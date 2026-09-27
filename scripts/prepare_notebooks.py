"""Insérer les cellules Colab communes et nettoyer les notebooks distribués."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "svngoku/cybersup-deep-learning-intro"
MANAGED = {"colab-link", "colab-instructions", "colab-setup", "results-instructions", "results-export"}


def cell(kind, source, role):
    item = {"cell_type": kind, "metadata": {"course_role": role}, "source": source.splitlines(keepends=True)}
    if kind == "code":
        item.update(execution_count=None, outputs=[])
    return item


def normalized(notebook, relative):
    # Une nouvelle structure est construite afin que --check ne modifie rien.
    notebook = json.loads(json.dumps(notebook))
    original = [c for c in notebook["cells"] if c.get("metadata", {}).get("course_role") not in MANAGED]
    first_code = next(i for i, c in enumerate(original) if c["cell_type"] == "code")
    link = f"https://colab.research.google.com/github/{REPO}/blob/main/{relative.as_posix()}"
    prefix = [cell("markdown", f"[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)]({link})\n", "colab-link")]
    setup = [
        cell("markdown", "## Préparation de l'environnement\n\nExécuter cette cellule en premier dans un runtime Python 3 sur **CPU**. Les bibliothèques déjà installées sont conservées ; seules celles qui manquent sont ajoutées. Aucun clonage, fichier voisin ou montage Drive n'est nécessaire. Enregistrer une copie du notebook avant de commencer. Si le lien vers le dépôt privé est inaccessible, importer le fichier fourni dans le pack étudiant.\n", "colab-instructions"),
        cell("code", (ROOT / "notebooks/_shared/colab_setup.py").read_text(encoding="utf-8"), "colab-setup"),
    ]
    suffix = [
        cell("markdown", "## Exporter les résultats\n\nExécuter la cellule suivante après le bilan terminal pour enregistrer métriques, graine et versions dans un fichier JSON. Dans Colab, activer `DOWNLOAD_RESULTS` pour le télécharger. Sauvegarder également une copie du notebook avec les sorties et les réponses aux investigations. Les fichiers du runtime sont temporaires.\n", "results-instructions"),
        cell("code", (ROOT / "notebooks/_shared/export_results.py").read_text(encoding="utf-8"), "results-export"),
    ]
    notebook["cells"] = prefix + original[:first_code] + setup + original[first_code:] + suffix
    for index, item in enumerate(notebook["cells"]):
        identifier = hashlib.sha256(f"{relative}:{index}".encode()).hexdigest()[:16]
        role = item.get("metadata", {}).get("course_role")
        item["id"] = identifier
        item["metadata"] = {"id": identifier, **({"course_role": role} if role else {})}
        if isinstance(item["source"], str):
            item["source"] = item["source"].splitlines(keepends=True)
        if item["cell_type"] == "code":
            item["execution_count"] = None
            item["outputs"] = []
    notebook["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
        "colab": {"name": relative.name, "provenance": [], "include_colab_link": True},
    }
    notebook.update(nbformat=4, nbformat_minor=5)
    return notebook


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--bootstrap", action="store_true", help="Importer les anciens notebooks de output/ une seule fois.")
    args = parser.parse_args()
    if args.check and args.bootstrap:
        parser.error("--check et --bootstrap sont exclusifs")
    if args.bootstrap:
        for source, target in [("TP-etudiants", "etudiants"), ("Corriges-formateur", "formateur")]:
            files = sorted((ROOT / "output" / source).glob("*.ipynb"))
            if len(files) != 5:
                raise ValueError(f"Cinq notebooks attendus dans {source}")
            destination = ROOT / "notebooks" / target
            destination.mkdir(parents=True, exist_ok=True)
            for path in files:
                output = destination / path.name
                if output.exists():
                    raise FileExistsError(f"Migration refusée : {output} existe déjà")
                output.write_bytes(path.read_bytes())
    paths = sorted((ROOT / "notebooks/etudiants").glob("*.ipynb")) + sorted((ROOT / "notebooks/formateur").glob("*.ipynb"))
    if len(paths) != 10:
        raise ValueError("Dix notebooks de référence sont attendus")
    for path in paths:
        data = normalized(json.loads(path.read_text(encoding="utf-8")), path.relative_to(ROOT))
        content = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
        if args.check:
            if path.read_text(encoding="utf-8") != content:
                raise ValueError(f"Régénérer {path.relative_to(ROOT)} avec prepare_notebooks.py")
        else:
            path.write_text(content, encoding="utf-8")
    print(f"{len(paths)} notebooks {'vérifiés' if args.check else 'préparés'}.")


if __name__ == "__main__":
    main()
