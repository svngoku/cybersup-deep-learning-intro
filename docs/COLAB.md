# Utiliser le cours dans Google Colab

## Pour le formateur

Les dix notebooks comportent une cellule de préparation autonome, un lien Colab et un export JSON. Ils n'ont pas besoin des fichiers voisins du dépôt. Les cinq TP utilisent explicitement le CPU ; choisir **Python 3**, sans GPU ni TPU.

Le dépôt étant privé, ouvrir le [sélecteur GitHub de Colab](https://colab.research.google.com/github), activer l'accès aux dépôts privés et s'authentifier avec le compte GitHub habilité si Colab le demande. Les boutons du README pointent vers la branche `main`. Cette procédure suit le [guide officiel Colab/GitHub](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb).

Pour préparer une séance sans relier son compte GitHub à Colab, télécharger le notebook puis l'importer comme un fichier local.

## Pour les étudiants

Distribuer uniquement `CYBERSUP-Deep-Learning-M2-Pack-etudiant.zip` et les [instructions étudiantes](ETUDIANTS.md). Ce pack permet d'importer les notebooks sans donner accès au dépôt complet. Un accès au dépôt privé donnerait aussi accès aux corrigés, aux notes et au PowerPoint.

Les étudiants enregistrent leur propre copie du notebook. Leur travail ne modifie pas la branche `main`. Pour les rendus, recueillir le `.ipynb` avec ses sorties et le fichier JSON produit en fin de TP.

## Bibliothèques et reproductibilité

La préparation teste la présence de NumPy, scikit-learn, PyTorch et Matplotlib avant les imports. Elle installe uniquement les paquets absents, aux versions de référence du cours. Elle ne remplace pas un PyTorch déjà présent dans Colab. Les versions effectives, Python et la disponibilité de CUDA sont affichés, puis joints au JSON ; le périphérique de calcul reste `cpu`.

`requirements.txt` fixe les versions utilisées pour la validation locale et la CI. Il n'est pas nécessaire d'exécuter `pip install -r requirements.txt` dans Colab. L'environnement hébergé évolue ; refaire une exécution complète avant chaque promotion et conserver les versions dans les rendus.

Le TP 03 peut montrer un transfert négatif : conserver et expliquer cette observation. Une différence avec les scores de référence ne justifie pas de modifier le protocole après lecture du test.

## Sauvegarde

Enregistrer une copie dans Drive ou télécharger le notebook. Le JSON d'expérience doit être téléchargé séparément depuis la dernière cellule ou le panneau Fichiers. Aucun montage du Drive n'est nécessaire. Le runtime et ses fichiers temporaires peuvent être supprimés entre les sessions ; voir la [FAQ officielle Colab](https://research.google.com/colaboratory/faq.html).

## Ce que vérifie la CI

- Validité des dix fichiers Jupyter, liens Colab, identifiants des cellules et absence de sorties préremplies.
- Identité des cellules de calcul entre chaque TP et son corrigé.
- Exécution complète des cinq TP dans des noyaux CPU indépendants, depuis des dossiers vides.
- Présence des résultats JSON et des versions, contrôle des gradients, des dimensions et de la causalité par les assertions des TP.
- Contenu des packs et absence de matériel formateur dans le pack étudiant.

Cette validation ne simule pas une connexion à un compte Google ni l'allocation d'un runtime Colab.
