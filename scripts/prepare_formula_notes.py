"""Synchroniser les explications des formules dans les sources et les notes."""
import argparse
import json
import posixpath
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def formula_notes(entry, markdown=False):
    lines = ["LECTURE À VOIX HAUTE", *["« " + line + " »" for line in entry["lecture"]], "",
             "SYMBOLES : NOM À PRONONCER ET SENS"]
    if markdown:
        lines += ["", "| Symbole | Nom à prononcer | Sens ici |", "| --- | --- | --- |"]
        for symbol, pronunciation, meaning in entry["symboles"]:
            values = [chr(96) + symbol + chr(96), "« " + pronunciation + " »", meaning]
            lines.append("| " + " | ".join(v.replace("|", r"\|") for v in values) + " |")
    else:
        lines.append("Symbole | Nom à prononcer | Sens ici")
        lines += [f"{s} | « {p} » | {m}" for s, p, m in entry["symboles"]]
    lines += ["", "INTERPRÉTATION", entry["sens"], "", "POINT D’ATTENTION", entry["attention"]]
    return "\n".join(lines)


def slide_notes(course, slide, number, markdown=False):
    title = slide["title"].replace("\n", " ")
    text = f"DIAPOSITIVE {number} — {title}\n\nEXPLICATION TECHNIQUE\n{slide['notes']}\n\n"
    if slide.get("math"):
        text += "ÉQUATION — SOURCE LATEX\n" + slide["math"] + "\n\n"
        text += formula_notes(slide["lecture_formule"], markdown) + "\n\n"
    if slide.get("question"):
        text += "QUESTION À POSER\n" + slide["question"] + "\n\nRÉPONSE ATTENDUE\n" + slide["answer"] + "\n\n"
    if slide["refs"]:
        text += "LECTURES ET RÉFÉRENCES\n" + "\n\n".join(
            "\n".join(course["sources"][key]) for key in slide["refs"])
    else:
        text += "EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX"
    return text


def sync(path, content, check):
    if check:
        if path.read_text() != content:
            raise ValueError(f"Fichier périmé : {path.relative_to(ROOT)}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


def note_parts(package):
    def relationships(owner):
        name = posixpath.join(posixpath.dirname(owner), "_rels", posixpath.basename(owner) + ".rels")
        return ET.fromstring(package.read(name))

    def target(owner, relationship):
        return posixpath.normpath(posixpath.join(posixpath.dirname(owner), relationship.attrib["Target"])).lstrip("/")

    owner = "ppt/presentation.xml"
    relationships_by_id = {r.attrib["Id"]: r for r in relationships(owner)}
    slides = ET.fromstring(package.read(owner)).find("p:sldIdLst", NS)
    result = []
    for slide in slides:
        path = target(owner, relationships_by_id[slide.attrib["{" + NS["r"] + "}id"]])
        note = next(r for r in relationships(path) if r.attrib["Type"].endswith("/notesSlide"))
        result.append(target(path, note))
    return result


def body_text(payload):
    tree = ET.fromstring(payload)
    for shape in tree.findall(".//p:sp", NS):
        placeholder = shape.find("p:nvSpPr/p:nvPr/p:ph", NS)
        if placeholder is not None and placeholder.get("type") == "body":
            body = shape.find("p:txBody", NS)
            return "\n".join("".join(p.itertext()) for p in body.findall("a:p", NS))
    raise ValueError("Notes sans emplacement de texte")


def verify_pptx(path, notes, base_path, changed):
    with ZipFile(path) as package:
        if package.testzip() is not None:
            raise ValueError("Archive PowerPoint corrompue")
        parts = note_parts(package)
        if len(parts) != len(notes):
            raise ValueError("Nombre de diapositives incorrect")
        for index, (part, expected) in enumerate(zip(parts, notes), 1):
            if body_text(package.read(part)) != expected:
                raise ValueError(f"Notes différentes de la source : diapositive {index}")
        if base_path:
            with ZipFile(base_path) as base:
                if set(base.namelist()) != set(package.namelist()):
                    raise ValueError("La structure du PowerPoint a changé")
                allowed = {parts[index - 1] for index in changed}
                actual = {name for name in base.namelist() if base.read(name) != package.read(name)}
                if actual != allowed:
                    raise ValueError(f"Pièces modifiées inattendues : {actual ^ allowed}")
                print(f"{len(actual)} notes modifiées ; toutes les autres pièces du PPTX sont identiques")
    print(f"{len(notes)} notes PowerPoint conformes aux sources")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--pptx", type=Path, help="Vérifier aussi les notes du PowerPoint indiqué")
    parser.add_argument("--base-pptx", type=Path, help="Vérifier que seules les notes ont changé")
    args = parser.parse_args()
    if args.base_pptx and not args.pptx:
        parser.error("--base-pptx nécessite --pptx")
    course = json.loads((OUT / "sources/cours.json").read_text())
    source = json.loads((OUT / "sources/lecture-formules.json").read_text())
    entries = source["formules"]
    expected = {i + 1 for i, slide in enumerate(course["slides"]) if slide.get("math")}
    if len(entries) != len(expected) or {f["slide"] for f in entries} != expected:
        raise ValueError("Chaque diapositive avec formule doit avoir exactement une fiche")
    for entry in entries:
        slide = course["slides"][entry["slide"] - 1]
        if entry["latex"] != slide["math"] or entry["title"] != slide["title"]:
            raise ValueError(f"Formule ou titre modifié : diapositive {entry['slide']}")
        if not entry["lecture"] or not all(isinstance(x, str) and x.strip() for x in entry["lecture"]):
            raise ValueError("Lecture à voix haute manquante")
        if not entry["symboles"] or not all(
            len(row) == 3 and all(isinstance(x, str) and x.strip() for x in row)
            for row in entry["symboles"]
        ) or not entry["sens"] or not entry["attention"]:
            raise ValueError("Tableau de symboles ou explications incomplets")
        slide["lecture_formule"] = {key: entry[key] for key in ["lecture", "symboles", "sens", "attention"]}
    notes = [slide_notes(course, s, i + 1) for i, s in enumerate(course["slides"])]
    guide = (
        "# Deep Learning — Guide du formateur\n\n"
        "Master 2 IA · Chrys NIONGOLO · 35 heures, cinq journées.\n\n"
        "Ce guide reprend les notes du PowerPoint. Chaque formule comporte une lecture à voix haute, "
        "un tableau des symboles avec leur prononciation et leur sens, une interprétation et un point d’attention. "
        "Ces explications sont réservées aux notes et au guide formateur ; elles n’ajoutent aucun contenu aux diapositives projetées. "
        "Les équations visibles restent composées depuis LaTeX. Les pauses sont à ajouter aux 420 minutes quotidiennes.\n\n"
    )
    for i, slide in enumerate(course["slides"], 1):
        guide += "## " + str(i) + ". " + slide["title"].replace("\n", " ") + "\n\n"
        if slide.get("table"):
            guide += "\n".join(" | ".join(row) for row in slide["table"]) + "\n\n"
        guide += slide_notes(course, slide, i, markdown=True) + "\n\n"
    sync(OUT / "sources/cours.json", json.dumps(course, ensure_ascii=False, indent=2) + "\n", args.check)
    sync(OUT / "Guide-formateur.md", guide, args.check)
    if not args.check:
        sync(ROOT / ".build/formula-notes/notes.json", json.dumps(notes, ensure_ascii=False, indent=2) + "\n", False)
    if args.pptx:
        verify_pptx(args.pptx, notes, args.base_pptx, expected)
    print(f"{len(entries)} formules : lecture, symboles, interprétation et point d’attention vérifiés")


if __name__ == "__main__":
    main()
