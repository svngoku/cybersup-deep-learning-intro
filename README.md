# Deep Learning — CNN et Transformers

[![Validation des notebooks](https://github.com/svngoku/cybersup-deep-learning-intro/actions/workflows/notebooks.yml/badge.svg)](https://github.com/svngoku/cybersup-deep-learning-intro/actions/workflows/notebooks.yml)

Cours d'introduction technique pour **Master 2 IA**, par **Chrys NIONGOLO** : **35 heures sur cinq journées**, 135 diapositives et cinq TP. Le template Cybersup est conservé ; son fichier source n'est pas publié dans le dépôt.

L'introduction présente les repères historiques du deep learning, les boucles d'apprentissage, les représentations et le choix d'une approche. Les deux schémas fournis du livre de Howard et Gugger sont intégrés avec leur attribution. Le deep learning est situé comme une famille du machine learning. Cette introduction est comprise dans le jour 1, dont le TP conserve ses 150 minutes.

## Démarrer dans Google Colab

Les notebooks sont autonomes : pas de clonage du dépôt, de montage Drive ni de téléchargement de données. La première cellule prépare les bibliothèques manquantes et affiche les versions réellement utilisées. Le **CPU** suffit aux cinq TP.

Ce dépôt est **privé** et contient les corrigés. Les liens ci-dessous sont destinés au formateur et aux personnes disposant de cet accès. Pour la classe, distribuer le [pack étudiant](output/CYBERSUP-Deep-Learning-M2-Pack-etudiant.zip), puis suivre les [instructions d'import dans Colab](docs/ETUDIANTS.md). Le pack contient uniquement le PDF, les cinq notebooks étudiants et leurs instructions.

| Jour | Thème et travail pratique | Durée du TP | Ouvrir |
| --- | --- | --- | --- |
| 1 | [MLP NumPy et rétropropagation](notebooks/etudiants/01_mlp_backprop.ipynb) | 150 min | [![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/svngoku/cybersup-deep-learning-intro/blob/main/notebooks/etudiants/01_mlp_backprop.ipynb) |
| 2 | [Optimisation et CNN sur digits](notebooks/etudiants/02_cnn_vision.ipynb) | 150 min | [![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/svngoku/cybersup-deep-learning-intro/blob/main/notebooks/etudiants/02_cnn_vision.ipynb) |
| 3 | [CNN et transfert d'apprentissage](notebooks/etudiants/03_transfer_learning.ipynb) | 180 min | [![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/svngoku/cybersup-deep-learning-intro/blob/main/notebooks/etudiants/03_transfer_learning.ipynb) |
| 4 | [Attention multi-têtes et masques](notebooks/etudiants/04_attention_masques.ipynb) | 150 min | [![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/svngoku/cybersup-deep-learning-intro/blob/main/notebooks/etudiants/04_attention_masques.ipynb) |
| 5 | [Mini-Transformer causal et patches](notebooks/etudiants/05_transformer_causal.ipynb) | 180 min | [![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/svngoku/cybersup-deep-learning-intro/blob/main/notebooks/etudiants/05_transformer_causal.ipynb) |

Chaque journée totalise 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les TP représentent **13 h 30**. Le cours comprend également des calculs au tableau, des exercices et des restitutions.

## Supports du cours

- [PowerPoint avec les notes techniques](output/CYBERSUP-Deep-Learning-M2-35h-v3.pptx) et [PDF des diapositives](output/CYBERSUP-Deep-Learning-M2-35h-v3.pdf).
- [Guide du formateur](output/Guide-formateur.md), [corrigés des notebooks](notebooks/formateur/) et [sources LaTeX](output/sources/formules.tex).
- [Pack étudiant](output/CYBERSUP-Deep-Learning-M2-Pack-etudiant.zip) et [pack formateur complet](output/CYBERSUP-Deep-Learning-M2-Pack-formateur.zip).
- [Guide Colab](docs/COLAB.md) : accès privé, sauvegarde, export des résultats et dépannage.

Dans PowerPoint, ouvrir le volet **Notes** ou le **mode Présentateur**. Les 69 équations sont composées depuis LaTeX et insérées en vectoriel ; les sources permettent de les modifier. Les textes et tableaux sont éditables. Les deux extraits O'Reilly restent des images et leurs [références sont documentées](output/sources/illustrations.md). Les polices du template sont Archivo Black, DM Sans et Roboto Mono. La version courante est la v3 ; la v2 est conservée comme version antérieure.

## Organisation du dépôt

```text
notebooks/etudiants/  cinq TP à modifier et à distribuer
notebooks/formateur/ cinq versions avec réponses et points de contrôle
notebooks/_shared/  cellules communes de préparation Colab et d'export
docs/                guides d'utilisation
output/              supports du cours, sources des slides et archives
scripts/             préparation, validation et construction des packs
.github/workflows/   validation automatique sur CPU
```

Les copies `output/TP-etudiants/` et `output/Corriges-formateur/` sont produites localement par les scripts ; les notebooks versionnés dans `notebooks/` font référence. Les sorties calculées sont retirées des notebooks distribués afin que les étudiants exécutent leurs propres expériences.

## Exécution locale et validation

Google Colab est l'environnement de travail de la classe. Pour développer ou reproduire les vérifications localement, utiliser Python 3.12 :

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user --name cybersup-dl --display-name "Cybersup Deep Learning"
python scripts/prepare_notebooks.py --check
python scripts/validate_notebooks.py --execute --kernel cybersup-dl
python scripts/build_packs.py --check
```

La CI contrôle les dix notebooks et exécute les cinq TP étudiants dans cinq noyaux indépendants, depuis des dossiers temporaires sans fichiers du dépôt. Elle vérifie aussi que les cellules de calcul des corrigés sont identiques à celles des TP. Les rapports d'exécution restent dans `.build/` et dans les artefacts de CI. Une validation Linux/Python ne constitue pas une exécution sur un runtime hébergé par Google Colab.

La cellule Colab conserve les bibliothèques déjà installées et affiche leurs versions ; `requirements.txt` fixe l'environnement local et celui de la CI. Les résultats et temps peuvent donc varier. L'extension ResNet des diapositives est distincte des TP : elle requiert torchvision et le téléchargement des poids.

Les notebooks donnent une base fonctionnelle, des contrôles et des investigations à mener. Choisir les configurations sur la validation et réserver le test au bilan terminal. Les jeux digits et synthétiques ne prouvent pas une performance en conditions réelles. Voir la [maintenance du cours](docs/MAINTENANCE.md) pour régénérer les fichiers.

## Références

- [Jeremy Howard et Sylvain Gugger, Deep Learning for Coders with fastai and PyTorch, O'Reilly, 2020](https://www.oreilly.com/library/view/deep-learning-for/9781492045519/), chapitre 1, figures 1-6 et 1-8 fournies par le formateur.
- [LeCun, Bengio et Hinton, Deep learning, 2015](https://www.nature.com/articles/nature14539). Les publications historiques sont citées dans les notes de l'introduction.
- [Jérémie Bigot, Introduction au Deep Learning](https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf).
- [Romain Tavenard, Introduction au Deep Learning](https://rtavenar.github.io/deep_book/book_fr.pdf) et [version HTML](https://rtavenar.github.io/deep_book/fr/content/fr/intro.html).
- [Javiera Castillo Navarro, RCP 209, CNAM](https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf).
- [Geoffrey Daniel, Réseaux de neurones et deep learning](https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf).
- [Vaswani et al., Attention Is All You Need](https://arxiv.org/abs/1706.03762), [He et al., Deep Residual Learning](https://arxiv.org/abs/1512.03385), [Dosovitskiy et al., Vision Transformer](https://arxiv.org/abs/2010.11929).
- [Documentation officielle : Colab et GitHub](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb), [FAQ Colab](https://research.google.com/colaboratory/faq.html).

Les autres références figurent dans les diapositives et leurs notes. Les exemples et notebooks ont été rédigés pour ce cours. Les PDF externes et le template original ne sont pas redistribués dans les packs.
