"""Vérifier les dix notebooks et exécuter les cinq TP autonomes sur CPU."""
import argparse
import ast
import json
import tempfile
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient

from prepare_notebooks import REPO, ROOT


def checked(path):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    assert notebook.metadata.kernelspec.name == "python3", path
    ids = [c.id for c in notebook.cells]
    assert len(ids) == len(set(ids)), path
    roles = [c.metadata.get("course_role") for c in notebook.cells]
    for role in ["colab-link", "colab-setup", "results-export"]:
        assert roles.count(role) == 1, (path, role)
    code = []
    for index, item in enumerate(notebook.cells):
        assert "/Users/" not in item.source and "/home/runner/" not in item.source, path
        if item.cell_type == "code":
            assert item.execution_count is None and not item.outputs, (path, index)
            ast.parse(item.source, filename=f"{path.name}:cell-{index}")
            code.append(item.source)
    expected = f"https://colab.research.google.com/github/{REPO}/blob/main/{path.relative_to(ROOT).as_posix()}"
    assert expected in notebook.cells[0].source, path
    assert "## Corrigé" not in "\n".join(c.source for c in notebook.cells) or "formateur" in path.parts, path
    return notebook, code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--kernel", default="python3")
    args = parser.parse_args()
    students = sorted((ROOT / "notebooks/etudiants").glob("*.ipynb"))
    teachers = sorted((ROOT / "notebooks/formateur").glob("*.ipynb"))
    assert len(students) == len(teachers) == 5
    notebooks = {}
    for path in students:
        notebook, code = checked(path)
        teacher = ROOT / "notebooks/formateur" / path.name.replace(".ipynb", "_corrige.ipynb")
        _, teacher_code = checked(teacher)
        assert teacher_code == code, f"Le code du corrigé diffère : {teacher.name}"
        notebooks[path] = notebook
    print("Structure et liens : 10 notebooks ; calculs identiques dans les corrigés.", flush=True)
    if not args.execute:
        return
    destination = ROOT / ".build/notebook-checks"
    destination.mkdir(parents=True, exist_ok=True)
    report = {"environment": "CPU local ou CI, hors runtime Colab hébergé", "checked": 10, "executed": []}
    for path, notebook in notebooks.items():
        started = time.monotonic()
        with tempfile.TemporaryDirectory(prefix="cybersup-dl-") as directory:
            NotebookClient(notebook, timeout=300, kernel_name=args.kernel,
                           resources={"metadata": {"path": directory}}, allow_errors=False).execute()
            result_files = list((Path(directory) / "resultats").glob("tp_*.json"))
            assert len(result_files) == 1, path
            result = json.loads(result_files[0].read_text(encoding="utf-8"))
            assert result["environment"]["device"] == "cpu", path
            assert result["seed"] == 42, path
            assert result["results"]["tp"] == int(path.name[:2]), path
            assert all(result["environment"].get(k) for k in ["python", "torch", "numpy", "scikit_learn", "matplotlib"])
            (destination / result_files[0].name).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        nbformat.write(notebook, destination / path.name)
        elapsed = round(time.monotonic() - started, 2)
        report["executed"].append({"notebook": path.name, "seconds": elapsed, "errors": 0})
        (destination / "validation.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"OK {path.name} ({elapsed}s)", flush=True)


if __name__ == "__main__":
    main()
