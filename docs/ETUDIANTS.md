# Démarrer les TP dans Google Colab

Cours de Deep Learning, Master 2 IA, par Chrys NIONGOLO. Le pack contient le PDF du cours et cinq notebooks, à travailler dans l'ordre 01 à 05. Les cellules donnent une base fonctionnelle ; les investigations et le compte rendu sont à réaliser.

## Ouvrir un notebook

1. Décompresser le pack fourni par le formateur.
2. Se connecter avec son compte Google à [Google Colab](https://colab.research.google.com/).
3. Dans **Fichier > Importer un notebook** (ou **Ouvrir un notebook > Importer**, selon l'interface), sélectionner un fichier `.ipynb` du dossier `notebooks` du pack. Ne pas importer le ZIP entier.
4. Enregistrer une copie dans son Drive et la renommer, par exemple `Nom_Prenom_TP01.ipynb`.
5. Conserver un environnement **Python 3 sur CPU**, sans accélérateur matériel.
6. Exécuter les cellules dans l'ordre, en commençant par **Préparation de l'environnement**.

Le dépôt GitHub du formateur est privé. L'import du fichier fourni dans le pack ne demande aucun accès à ce dépôt. Les boutons GitHub/Colab présents dans les notebooks sont réservés aux personnes disposant de cet accès ; utiliser l'import ci-dessus si nécessaire.

Les TP utilisent digits, inclus dans scikit-learn, ou des données générées sur place. Aucun compte Hugging Face, jeton d'API, montage Drive ou clonage Git n'est requis. Une connexion Internet et un compte Google sont nécessaires pour Colab.

## Conserver son travail

Renseigner les réponses dans les cellules Markdown et commenter chaque expérience : hypothèse, configuration, résultat de validation et interprétation. Garder la graine et le budget de calcul visibles.

En fin de TP, la cellule **Exporter les résultats** écrit un fichier JSON dans `resultats/`, avec les métriques, la graine et les versions. Dans Colab, cocher `DOWNLOAD_RESULTS`, puis réexécuter cette cellule pour télécharger le JSON. Le panneau **Fichiers** permet aussi de le télécharger. Les fichiers du runtime sont temporaires ; enregistrer le notebook dans Drive ou télécharger une copie `.ipynb` avant de fermer la session.

Remettre au formateur le notebook avec les sorties, le JSON et un court bilan des expériences. Ne choisir aucun réglage sur le score test.

## En cas d'erreur

- Après une reconnexion, réexécuter depuis le début : les variables d'une ancienne session ne sont pas conservées.
- Si les imports échouent, relancer un runtime neuf puis la cellule de préparation. Transmettre au formateur le message complet et les versions affichées.
- Un GPU ne rendra pas automatiquement ces petits TP plus rapides ; les calculs sont explicitement effectués sur CPU.

Une exécution locale reste possible avec Python 3.12 et `python -m pip install -r requirements.txt`, puis Jupyter ou VS Code.
