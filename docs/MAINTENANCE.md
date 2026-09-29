# Maintenir les supports

Les notebooks de référence sont dans `notebooks/etudiants/` et `notebooks/formateur/`. Modifier les deux versions lorsqu'une cellule de calcul change ; les réponses restent uniquement dans la version formateur.

Les cellules communes proviennent de `notebooks/_shared/colab_setup.py` et `notebooks/_shared/export_results.py`. Elles sont copiées dans chaque notebook afin que celui-ci reste autonome après import dans Colab.

Après une modification, depuis un environnement installé avec `requirements.txt` :

```sh
python scripts/prepare_notebooks.py
python scripts/validate_notebooks.py --execute
python scripts/build_packs.py
python scripts/build_packs.py --check
git diff --check
```

Préciser `--kernel cybersup-dl` pour utiliser le noyau local installé avec ce nom. Les exécutions utilisent des répertoires temporaires vides, et les rapports sont placés dans `.build/`. Les notebooks versionnés restent sans sorties.

`prepare_notebooks.py --check` vérifie que les notebooks correspondent aux cellules communes sans modifier de fichier. Le mode `--bootstrap` sert uniquement à la migration initiale des anciens notebooks du dossier `output/`.

`build_packs.py` crée les deux ZIP avec une liste explicite de fichiers. Le pack étudiant ne contient ni corrigés, ni guide formateur, ni PPTX, ni données JSON du cours avec les réponses. Les miroirs locaux `output/TP-etudiants/` et `output/Corriges-formateur/` sont également mis à jour.

Les présentations et leurs sources sont dans `output/`. Le générateur des packs ne reconstruit pas les slides. Le template original, les environnements locaux, les rapports, les clés et les fichiers `.env` restent hors de Git. Ne rendre public ce dépôt contenant les corrigés qu'après avoir préparé une distribution distincte adaptée.

La version courante est `CYBERSUP-Deep-Learning-M2-35h-v4` (135 diapositives). Les diapositives 3 à 12 forment l'introduction, avec les extraits fournis aux diapositives 7 et 8. Les références et la provenance figurent dans `output/sources/illustrations.md`. Conserver les proportions des images et leurs attributions. Après une modification des slides, synchroniser le PPTX, son PDF, les notes du guide, `sources/cours.json` et les sources LaTeX, puis reconstruire les deux packs. Les tableaux quotidiens doivent toujours totaliser 420 minutes chacun.

Les lectures des formules sont rédigées dans `output/sources/lecture-formules.json`. Chaque entrée associe le numéro de slide et sa formule LaTeX à une lecture complète, aux trois champs de chaque symbole, à une interprétation et à un point d’attention. Elles figurent uniquement dans les notes et leur miroir privé dans le guide formateur.

Après édition, exécuter `python scripts/prepare_formula_notes.py` pour synchroniser `cours.json`, le guide et le texte des notes dans `.build/formula-notes/notes.json`. La commande `python scripts/prepare_formula_notes.py --check` contrôle leur cohérence. Ce script ne reconstruit pas le PowerPoint : intégrer ensuite les textes aux notes du PPTX, puis vérifier avec `python scripts/prepare_formula_notes.py --check --pptx output/CYBERSUP-Deep-Learning-M2-35h-v4.pptx`. Pour une révision des seules notes, l’option `--base-pptx` contrôle que toutes les autres pièces de la présentation sont inchangées. Reconstruire les packs après toute modification.

La CI s'exécute sur les poussées vers `main`, les pull requests et à la demande. Elle utilise Python 3.12 et les roues PyTorch CPU. L'artefact `notebooks-cpu` contient les notebooks exécutés et les résultats de cette exécution.
