"""Construire les packs depuis des listes explicites et contrôler leur contenu."""
import argparse
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
PDF = "CYBERSUP-Deep-Learning-M2-35h-v4.pdf"
PPTX = "CYBERSUP-Deep-Learning-M2-35h-v4.pptx"


def expected_files():
    students = sorted((ROOT / "notebooks/etudiants").glob("*.ipynb"))
    teachers = sorted((ROOT / "notebooks/formateur").glob("*.ipynb"))
    if len(students) != 5 or len(teachers) != 5:
        raise ValueError("Cinq TP et cinq corrigés sont attendus")
    student = {"LIRE-AVANT.md": ROOT / "docs/ETUDIANTS.md", "requirements.txt": ROOT / "requirements.txt", PDF: OUT / PDF}
    student.update({"notebooks/" + p.name: p for p in students})
    # La liste reste fermée : aucun parcours récursif arbitraire du workspace.
    selected = [ROOT / "README.md", ROOT / "requirements.txt", OUT / PDF, OUT / PPTX, OUT / "Guide-formateur.md"]
    selected += students + teachers
    selected += sorted((ROOT / "docs").glob("*.md"))
    selected += sorted((ROOT / "notebooks/_shared").glob("*.py"))
    selected += sorted((ROOT / "scripts").glob("*.py"))
    selected += [OUT / "sources/formules.tex", OUT / "sources/cours.json", OUT / "sources/lecture-formules.json"]
    selected += [OUT / "sources/illustrations.md"]
    selected += sorted((OUT / "sources/images").glob("*.png"))
    teacher = {p.relative_to(ROOT).as_posix(): p for p in selected}
    return student, teacher


def archive(path, base, files, check):
    expected = {base + "/" + name: source for name, source in files.items()}
    if check:
        with ZipFile(path) as zipped:
            assert zipped.testzip() is None, path
            assert len(zipped.namelist()) == len(expected) and set(zipped.namelist()) == set(expected), path
            for name, source in expected.items():
                assert zipped.read(name) == source.read_bytes(), f"Archive périmée : {name}"
    else:
        with ZipFile(path, "w", compression=ZIP_DEFLATED) as zipped:
            for name, source in sorted(expected.items()):
                info = ZipInfo(name, date_time=(2026, 9, 27, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zipped.writestr(info, source.read_bytes())
    print(f"{path.name} : {len(expected)} fichiers {'vérifiés' if check else 'assemblés'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    student, teacher = expected_files()
    assert sum(name.endswith(".ipynb") for name in student) == 5
    assert not any(word in name.lower() for name in student for word in ["corrige", "formateur", ".pptx", ".tex"])
    for files in [student, teacher]:
        assert all(p.is_file() for p in files.values())
    archive(OUT / "CYBERSUP-Deep-Learning-M2-Pack-etudiant.zip", "CYBERSUP-Deep-Learning-Etudiant", student, args.check)
    archive(OUT / "CYBERSUP-Deep-Learning-M2-Pack-formateur.zip", "CYBERSUP-Deep-Learning-Formateur", teacher, args.check)
    if not args.check:
        for source, target in [("etudiants", "TP-etudiants"), ("formateur", "Corriges-formateur")]:
            destination = OUT / target
            destination.mkdir(parents=True, exist_ok=True)
            for notebook in sorted((ROOT / "notebooks" / source).glob("*.ipynb")):
                shutil.copyfile(notebook, destination / notebook.name)
            shutil.copyfile(ROOT / "requirements.txt", destination / "requirements.txt")
        shutil.copyfile(ROOT / "docs/ETUDIANTS.md", OUT / "TP-etudiants/LIRE-AVANT.md")


if __name__ == "__main__":
    main()
