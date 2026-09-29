# Deep Learning — Guide du formateur

Master 2 IA · Chrys NIONGOLO · 35 heures, cinq journées.

Ce guide reprend les notes du PowerPoint. Chaque formule comporte une lecture à voix haute, un tableau des symboles avec leur prononciation et leur sens, une interprétation et un point d’attention. Ces explications sont réservées aux notes et au guide formateur ; elles n’ajoutent aucun contenu aux diapositives projetées. Les équations visibles restent composées depuis LaTeX. Les pauses sont à ajouter aux 420 minutes quotidiennes.

## 1. DEEP LEARNING

DIAPOSITIVE 1 — DEEP LEARNING

EXPLICATION TECHNIQUE
Présenter les trois compétences visées : calculer et interpréter les gradients d'un réseau profond, construire un CNN adapté à un problème de vision et expliquer chaque opération d'un Transformer. Le fil conducteur est une même chaîne de raisonnement : définir les entrées et les sorties, écrire les opérations, choisir une perte, calculer ses gradients, puis vérifier la généralisation. Préciser que les petits modèles des TP servent à isoler les mécanismes. Ils ne reproduisent ni le coût ni les capacités d'un modèle de fondation.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 2. SOMMAIRE

DIAPOSITIVE 2 — SOMMAIRE

EXPLICATION TECHNIQUE
L’introduction situe le deep learning dans le machine learning et présente les deux boucles d’apprentissage du livre de Howard et Gugger. Elle est comprise dans le jour 1, et ne constitue pas une sixième journée. Le cours suit cinq journées de sept heures de formation effective, hors pauses. Chaque journée contient un TP exécuté sur CPU, des exercices mathématiques et une restitution. Les supports de Bigot, Tavenard, du CNAM et de Geoffrey Daniel servent de lectures complémentaires. Les articles originaux complètent la partie architectures. Les exemples numériques, exercices et notebooks de ce support sont construits pour cette progression. Inviter les étudiants à conserver un carnet des dimensions, hypothèses et observations.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

Geoffrey Daniel — Réseaux de neurones et deep learning : utilisation et méthodologie
https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf

## 3. REPÈRES ET PRINCIPES

DIAPOSITIVE 3 — REPÈRES ET PRINCIPES

EXPLICATION TECHNIQUE
Cette introduction prend environ 35 à 40 minutes à l’intérieur du cadrage du jour 1. Partir d’un problème concret : reconnaître une catégorie à partir des pixels d’une image. Demander ce que l’algorithme doit ajuster et ce que le concepteur doit choisir. Le deep learning appartient au machine learning. Le point de comparaison utile porte sur la construction des représentations, l’architecture et les paramètres optimisés. Les deux schémas du livre décrivent une boucle d’apprentissage commune, à deux niveaux de détail. Ils permettront ensuite de situer précisément les CNN et les Transformers. Les repères historiques proposés sont sélectifs : ils expliquent les idées utilisées dans le cours sans prétendre raconter une succession exhaustive d’inventions.

QUESTION À POSER
Dans un système de classification, quelles décisions relèvent des données et lesquelles relèvent du concepteur ?

RÉPONSE ATTENDUE
Les paramètres sont estimés à partir des données selon un objectif. La tâche, la collecte, l’architecture, le protocole et les contraintes restent des choix de conception.

LECTURES ET RÉFÉRENCES
Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

LeCun, Bengio et Hinton — Deep learning, Nature, 2015
https://www.nature.com/articles/nature14539

## 4. LE DEEP LEARNING DANS LE MACHINE LEARNING

DIAPOSITIVE 4 — LE DEEP LEARNING DANS LE MACHINE LEARNING

EXPLICATION TECHNIQUE
Définir le machine learning comme un ensemble de méthodes qui tirent des régularités des données pour accomplir une tâche. Il comprend notamment les modèles linéaires, les arbres, les méthodes à noyaux et les réseaux de neurones. Dans ce cours, le deep learning désigne l’apprentissage avec des réseaux comportant plusieurs transformations paramétrées successives. L’inclusion affichée est une carte des domaines, pas une échelle de qualité. Il n’existe pas de seuil universel de couches qui rendrait un modèle efficace ou pertinent. La profondeur d’un arbre de décision ne suffit pas à en faire un modèle de deep learning. Les transformations internes peuvent être apprises avec ou sans étiquettes externes. Notre première comparaison utilise l’apprentissage supervisé pour rendre la cible et la perte explicites. Une représentation apprise n’est pas forcément interprétable par un nom d’objet ou de contour.

ÉQUATION — SOURCE LATEX
\mathrm{Deep\ learning}\subset\mathrm{Machine\ learning}\subset\mathrm{IA}

LECTURE À VOIX HAUTE
« Le deep learning est inclus dans le machine learning, qui est lui-même inclus dans l’intelligence artificielle. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\mathrm{Deep\ learning}` | « deep learning, ou apprentissage profond » | Famille de méthodes fondées ici sur des réseaux à plusieurs niveaux de représentation. |
| `\mathrm{Machine\ learning}` | « machine learning, ou apprentissage automatique » | Domaine qui regroupe les méthodes apprenant à partir de données. |
| `\mathrm{IA}` | « i a » | Intelligence artificielle. |
| `\subset` | « est inclus dans » | Relation entre domaines. Tout élément du domaine de gauche appartient au domaine de droite. |

INTERPRÉTATION
L’écriture situe des familles de méthodes. Elle ne donne pas un classement de leurs performances.

POINT D’ATTENTION
Le signe d’inclusion ne se lit pas « inférieur à ».

QUESTION À POSER
Un arbre de décision très profond est-il un réseau de deep learning ?

RÉPONSE ATTENDUE
Non. Sa profondeur compte des décisions successives dans un arbre. Elle ne correspond pas à la composition de couches paramétrées d’un réseau.

LECTURES ET RÉFÉRENCES
LeCun, Bengio et Hinton — Deep learning, Nature, 2015
https://www.nature.com/articles/nature14539

Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

## 5. REPÈRES HISTORIQUES : LES FONDEMENTS

Date | Repère | Idée utile pour ce cours
1958 | Perceptron, Rosenblatt | Ajuster une règle de décision à partir d’exemples
1986 | Rétropropagation | Popularisation de l’apprentissage des couches cachées
1998 | LeNet-5 | Convolutions et paramètres partagés pour les chiffres
2006 | Deep belief networks | Préentraînement couche par couche des réseaux profonds

DIAPOSITIVE 5 — REPÈRES HISTORIQUES : LES FONDEMENTS

EXPLICATION TECHNIQUE
En 1958, Rosenblatt formalise le perceptron. Pour le cours, retenir l’idée d’une règle dont les paramètres changent avec les exemples. Le modèle linéaire simple ne résout pas tous les problèmes de séparation. L’article de Rumelhart, Hinton et Williams en 1986 montre comment l’erreur de sortie permet d’ajuster des unités cachées. Il popularise la rétropropagation dans les réseaux, sans constituer le début de toute différentiation inverse. LeNet-5, décrit en 1998, associe des connexions locales, le partage des poids et la réduction spatiale pour la reconnaissance de documents. Le travail de Hinton, Osindero et Teh en 2006 propose un entraînement des deep belief networks par étapes, puis un ajustement. Ce jalon rappelle que la difficulté ne se résume pas à écrire davantage de couches : il faut aussi réussir leur optimisation. Ces dates désignent les publications citées, pas une revendication d’invention exclusive.

QUESTION À POSER
Pourquoi l’existence d’une architecture expressive ne suffit-elle pas ?

RÉPONSE ATTENDUE
Il faut trouver des paramètres utiles avec des données et un algorithme d’apprentissage réalisables. Expressivité et facilité d’optimisation sont différentes.

LECTURES ET RÉFÉRENCES
Rosenblatt — The perceptron: a probabilistic model for information storage and organization in the brain, 1958
https://doi.org/10.1037/h0042519

Rumelhart, Hinton et Williams — Learning representations by back-propagating errors, 1986
https://doi.org/10.1038/323533a0

LeCun, Bottou, Bengio et Haffner — Gradient-Based Learning Applied to Document Recognition, 1998
https://bottou.org/papers/lecun-98h

Hinton, Osindero et Teh — A fast learning algorithm for deep belief nets, 2006
https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf

## 6. REPÈRES HISTORIQUES : LE PASSAGE À L’ÉCHELLE

Publication | Architecture | Apport étudié
2012 | AlexNet | CNN, données ImageNet et entraînement sur GPU
2017 | Transformer | Attention pour relier les positions d’une séquence
2020 / 2021 | Vision Transformer | Images découpées en patches et préentraînement

DIAPOSITIVE 6 — REPÈRES HISTORIQUES : LE PASSAGE À L’ÉCHELLE

EXPLICATION TECHNIQUE
AlexNet combine plusieurs facteurs en 2012 : un CNN, un grand jeu d’images annotées, une implémentation efficace sur GPU et des choix d’optimisation et de régularisation. Éviter d’attribuer le résultat à la profondeur seule. En 2017, le Transformer présenté pour la traduction utilise l’attention dans une architecture encodeur-décodeur, sans récurrence ni convolution pour traiter la séquence. L’attention existait auparavant : la nouveauté porte sur cette organisation complète du modèle. Le Vision Transformer transpose ensuite une architecture de type Transformer à des patches d’image. La prépublication est datée de 2020 et la publication de conférence de 2021. Les résultats du papier s’inscrivent dans un régime de préentraînement important. Ces repères motivent notre progression CNN puis attention. Une architecture plus récente ne remplace pas automatiquement une ancienne méthode pour chaque tâche. Le budget, les données, le préentraînement et le protocole conditionnent toute comparaison.

QUESTION À POSER
Peut-on comparer deux architectures uniquement à partir de leur année de publication ?

RÉPONSE ATTENDUE
Non. Il faut comparer leurs résultats pour une tâche donnée, avec le protocole, les données et les budgets explicités.

LECTURES ET RÉFÉRENCES
Krizhevsky, Sutskever et Hinton — ImageNet Classification with Deep Convolutional Neural Networks, 2012
https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html

Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

Dosovitskiy et al. — An Image is Worth 16x16 Words, 2020
https://arxiv.org/abs/2010.11929

## 7. LA BOUCLE D’APPRENTISSAGE

DIAPOSITIVE 7 — LA BOUCLE D’APPRENTISSAGE

EXPLICATION TECHNIQUE
Lire le schéma fourni de gauche à droite. Inputs désigne les observations. Weights désigne les coefficients ajustables. Model combine l’entrée et ces coefficients pour produire Results. Performance fournit un signal qui guide la modification des poids. Revenir ensuite sur la flèche Update : elle appartient à l’entraînement, pendant lequel on cherche des paramètres utiles. Les auteurs présentent ici une abstraction du processus d’apprentissage, pas une architecture neuronale particulière. Dans une implémentation par gradient, le signal optimisé sera une perte numérique. Le mot performance reste volontairement général dans cette première figure. La métrique communiquée au métier, telle que l’accuracy, peut être différente du critère utilisé par l’optimiseur. Cette boucle s’applique aussi à des modèles peu profonds. Un algorithme d’arbre apprend également à partir des données, avec une procédure de construction différente de la rétropropagation. Ne pas présenter cette figure comme exclusivement réservée au machine learning classique.

QUESTION À POSER
Quelle partie du schéma cesse de fonctionner pendant une simple prédiction sur une nouvelle image ?

RÉPONSE ATTENDUE
La mise à jour des paramètres. On conserve le calcul entrée-modèle-sortie avec les paramètres entraînés.

LECTURES ET RÉFÉRENCES
Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

Howard et Gugger — Chapitre 1, version des auteurs, figures Training a machine learning model et Detailed training loop
https://github.com/fastai/fastbook/blob/master/01_intro.ipynb

## 8. LA PERTE ET LA MISE À JOUR DES PARAMÈTRES

DIAPOSITIVE 8 — LA PERTE ET LA MISE À JOUR DES PARAMÈTRES

EXPLICATION TECHNIQUE
Relier cette figure à la précédente : Architecture avec Parameters constitue le Model. Predictions précise le rôle de Results et Loss explicite le signal d’apprentissage. Labels représente les cibles du cas supervisé illustré. Les paramètres incluent les poids et les biais. L’architecture fixe les opérations et les connexions, tandis que l’entraînement ajuste leurs paramètres. Dans nos réseaux différentiables, le calcul direct produit la perte, la rétropropagation calcule ses dérivées par rapport aux paramètres et l’optimiseur effectue la mise à jour. Ces trois opérations sont distinctes. L’architecture et les hyperparamètres se choisissent généralement à l’aide d’une validation externe à cette boucle d’ajustement. À l’inférence, le modèle n’a pas besoin de l’étiquette inconnue de l’exemple à prédire. Une étiquette peut être recueillie plus tard pour évaluer la prédiction. La figure est compatible avec un modèle linéaire différentiable : elle ne définit donc pas à elle seule le deep learning. L’auto-supervision construit les cibles à partir des données selon un protocole adapté.

QUESTION À POSER
La rétropropagation et l’optimiseur jouent-ils le même rôle ?

RÉPONSE ATTENDUE
Non. La rétropropagation calcule les gradients. L’optimiseur les utilise pour modifier les paramètres, avec son taux d’apprentissage et son éventuel état.

LECTURES ET RÉFÉRENCES
Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

Howard et Gugger — Chapitre 1, version des auteurs, figures Training a machine learning model et Detailed training loop
https://github.com/fastai/fastbook/blob/master/01_intro.ipynb

## 9. LE RÔLE DES REPRÉSENTATIONS

DIAPOSITIVE 9 — LE RÔLE DES REPRÉSENTATIONS

EXPLICATION TECHNIQUE
Définir N exemples étiquetés, x les observations, y les cibles et ell la perte. Dans la première ligne, phi est un descripteur fixé pour l’expérience. Seuls les paramètres theta du prédicteur g sont optimisés. Dans la seconde, h est un extracteur paramétré par psi. Si h et g sont différentiables, la règle de la chaîne permet d’ajuster psi et theta à partir d’un même objectif. Le gradient reçu par une couche dépend donc des transformations situées entre cette couche et la perte. C’est le sens de l’apprentissage de bout en bout. Cette comparaison concerne deux pipelines précis, pas toutes les méthodes de ML contre toutes les méthodes de DL. La PCA apprend déjà une représentation, les méthodes à noyaux changent l’espace de représentation, et un extracteur profond préentraîné peut être gelé. La formule du bas n’impose pas à elle seule la profondeur : celle-ci vient de la composition interne de h. Les prétraitements, la collecte et le choix de l’objectif restent nécessaires.

ÉQUATION — SOURCE LATEX
\begin{aligned}\text{Descripteur fixe :}\quad &\min_{\theta}\frac{1}{N}\sum_{i=1}^{N}\ell\bigl(g_{\theta}(\phi(x_i)),y_i\bigr)\\[8pt]\text{Repr. apprise :}\quad &\min_{\psi,\theta}\frac{1}{N}\sum_{i=1}^{N}\ell\bigl(g_{\theta}(h_{\psi}(x_i)),y_i\bigr)\end{aligned}

LECTURE À VOIX HAUTE
« Descripteur fixe : on minimise, par rapport à thêta, un sur grand N fois la somme, pour i allant de un à grand N, de la perte entre g thêta appliqué à phi de x i et la cible y i. »
« Représentation apprise : on minimise la même moyenne par rapport à psi et à thêta, avec h psi de x i comme représentation. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `N,\ i` | « grand n, i » | Nombre d’exemples et indice d’un exemple. |
| `x_i,\ y_i` | « x indice i, y indice i » | Observation et cible du i-ième exemple. |
| `\phi(x_i)` | « phi de x indice i » | Descripteur fixé dans cette comparaison. |
| `h_\psi(x_i)` | « h paramétré par psi, appliqué à x indice i » | Extracteur de représentation dont les paramètres sont psi. |
| `g_\theta` | « g paramétré par thêta » | Prédicteur dont les paramètres sont theta. |
| `\ell(\cdot,\cdot)` | « ell de deux arguments » | Perte qui compare une prédiction et sa cible. |
| `\frac1N\sum_{i=1}^N` | « un sur grand n fois la somme pour i de un à grand n » | Moyenne des pertes sur les exemples. |
| `\min_\theta,\ \min_{\psi,\theta}` | « minimum par rapport à thêta ; minimum par rapport à psi et thêta » | Variables ajustées par l’optimisation. |
| `g_\theta(h_\psi(x_i))` | « g thêta de h psi de x i » | On calcule d’abord la représentation h, puis la prédiction g. |

INTERPRÉTATION
La différence porte sur les paramètres que la perte peut ajuster : seulement le prédicteur, ou aussi l’extracteur.

POINT D’ATTENTION
Min désigne la valeur minimale recherchée. Arg min désignerait les paramètres qui la réalisent. Phi est ici une fonction fixe, alors qu’il désigne des paramètres dans la formule du transfert.

QUESTION À POSER
Que devient la seconde optimisation si l’extracteur préentraîné est gelé ?

RÉPONSE ATTENDUE
Psi reste constant. On optimise seulement theta, même si le calcul des caractéristiques utilise un réseau profond.

LECTURES ET RÉFÉRENCES
LeCun, Bengio et Hinton — Deep learning, Nature, 2015
https://www.nature.com/articles/nature14539

Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

## 10. DEUX PIPELINES POUR CLASSER UNE IMAGE

Étape | Descripteur fixe + classifieur | CNN entraîné de bout en bout
Entrée | Pixels, taille et normalisation | Pixels, taille et normalisation
Représentation | HOG : gradients et histogrammes | Cartes calculées par des filtres appris
Paramètres ajustés | Poids du classifieur | Filtres et tête de classification
Choix humains | Descripteur et modèle | Architecture, perte et données

DIAPOSITIVE 10 — DEUX PIPELINES POUR CLASSER UNE IMAGE

EXPLICATION TECHNIQUE
Prendre une même collection d’images annotées et fixer les partitions avant toute comparaison. Dans un pipeline utilisant HOG, on calcule des gradients locaux puis des histogrammes d’orientations avec des normalisations. La recette du descripteur est conçue à l’avance, puis un classifieur apprend sur les vecteurs obtenus. Le travail historique de Dalal et Triggs utilise notamment un SVM linéaire pour la détection de personnes. Le tableau transpose l’idée de représentation à un exemple pédagogique de classification d’images. Dans un CNN entraîné de bout en bout, les valeurs des filtres et les paramètres de la tête changent sous l’effet de la perte. Le concepteur choisit toujours la résolution, les transformations autorisées, l’architecture et le protocole. Le réseau ne supprime donc pas toute ingénierie. Pour une comparaison honnête, documenter aussi le préentraînement éventuel et le budget. Les niveaux internes d’un CNN n’ont pas nécessairement une interprétation sémantique simple ou universelle.

QUESTION À POSER
Quelle expérience isole l’effet des représentations ?

RÉPONSE ATTENDUE
Comparer des extracteurs avec une tête et un protocole contrôlés, puis expliciter ce qui change en dimension, préentraînement, données et coût.

LECTURES ET RÉFÉRENCES
Dalal et Triggs — Histograms of Oriented Gradients for Human Detection, 2005
https://doi.org/10.1109/CVPR.2005.177

LeCun, Bottou, Bengio et Haffner — Gradient-Based Learning Applied to Document Recognition, 1998
https://bottou.org/papers/lecun-98h

LeCun, Bengio et Hinton — Deep learning, Nature, 2015
https://www.nature.com/articles/nature14539

## 11. LE CHOIX D’UNE APPROCHE

Situation | Point de départ à comparer | Critère décisif
Données tabulaires
peu nombreuses | Modèle linéaire ou arbres | Validation, stabilité et coût
Images ou texte
avec modèle adapté | Réseau préentraîné, puis adaptation | Gain observé et compatibilité du domaine
Peu d’étiquettes
pour la tâche cible | Extracteur préentraîné gelé
et tête simple | Qualité des représentations transférées

DIAPOSITIVE 11 — LE CHOIX D’UNE APPROCHE

EXPLICATION TECHNIQUE
Présenter ce tableau comme une démarche de comparaison, pas comme un classement universel. Sur un petit tableau structuré, une méthode simple fournit un résultat de référence rapide à mesurer. Cela ne prouve pas que les réseaux échoueront : on demande un gain validé avant d’accepter leur coût supplémentaire. Sur des images ou du texte, un modèle préentraîné peut fournir des représentations utiles, si son domaine et ses entrées sont compatibles avec la tâche cible. Avec peu d’étiquettes, geler l’extracteur réduit le nombre de paramètres ajustés. Ce choix n’élimine pas le décalage de distribution. Distinguer le besoin en données du préentraînement initial et celui de l’adaptation locale. Il n’existe pas un nombre magique d’exemples à partir duquel le deep learning devient obligatoire. Pour chaque candidat, mesurer le score de validation, sa variabilité, la latence et la mémoire. Ces recommandations sont des points de départ pédagogiques à confirmer sur les données du projet.

QUESTION À POSER
Pourquoi un réseau préentraîné peut-il être utilisable avec peu d’étiquettes locales ?

RÉPONSE ATTENDUE
Une partie des représentations a déjà été apprise sur d’autres données. Leur utilité pour la cible doit être vérifiée et le préentraînement doit être documenté.

LECTURES ET RÉFÉRENCES
Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

## 12. UN PROTOCOLE EXPÉRIMENTAL COMMUN

DIAPOSITIVE 12 — UN PROTOCOLE EXPÉRIMENTAL COMMUN

EXPLICATION TECHNIQUE
Revenir au niveau du projet complet. Les diagrammes du livre décrivent la boucle d’ajustement du modèle, qui n’est qu’une partie du processus. Avant elle, il faut définir la population visée, les cibles et la manière de séparer les données. Une série temporelle ou des observations de plusieurs personnes ne se découpent pas forcément de façon aléatoire ligne par ligne. Les statistiques de normalisation et les représentations apprises pendant notre expérience doivent être ajustées sur le train, sauf préentraînement externe explicitement documenté. La validation permet les décisions d’architecture et d’hyperparamètres. Le test reste réservé au bilan du choix final. L’entropie croisée peut servir de perte tandis que l’accuracy ou le rappel répond à une question d’évaluation. Après déploiement, vérifier si les données et les erreurs changent. Ce cadre s’applique aux arbres, aux modèles linéaires, aux CNN et aux Transformers. Il servira de protocole commun aux cinq notebooks Colab.

QUESTION À POSER
Normaliser toutes les données avant le découpage est-il acceptable parce que les étiquettes ne sont pas utilisées ?

RÉPONSE ATTENDUE
Non. Les statistiques des partitions de validation et de test influenceraient la transformation. Ajuster la normalisation sur le train puis l’appliquer aux autres partitions.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

Jeremy Howard et Sylvain Gugger — Deep Learning for Coders with fastai and PyTorch, O’Reilly Media, 2020, chapitre 1
https://www.oreilly.com/library/view/deep-learning-for/9781492045519/

## 13. OBJECTIFS ET PREUVES DE MAÎTRISE

Objectif | Preuve attendue
Rétropropagation | Dérivation, dimensions et contrôle numérique
CNN pour la vision | Architecture, entraînement et analyse des erreurs
Transfert | Comparaison source / cible et stratégies de gel
Transformer | Attention, masque causal et boucle autoregressive
Démarche expérimentale | Validation séparée, ablations et limites explicites

DIAPOSITIVE 13 — OBJECTIFS ET PREUVES DE MAÎTRISE

EXPLICATION TECHNIQUE
Une compétence est acquise lorsque l'étudiant peut justifier son résultat et diagnostiquer un échec. Pour la rétropropagation, une dérivée mémorisée ne suffit pas : il faut relier chaque facteur à une opération du calcul direct. Pour les CNN, contrôler les tailles et le nombre de paramètres avant l'entraînement. Pour les Transformers, reconstruire le chemin Q, K, V et expliquer ce que le masque interdit. Les productions des TP seront évaluées sur la validité du protocole, la justesse technique et l'interprétation, sans seuil arbitraire de précision.

QUESTION À POSER
Que prouve une bonne accuracy sur le jeu d’entraînement ?

RÉPONSE ATTENDUE
La capacité à ajuster ces exemples ; elle ne prouve pas la généralisation.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 14. PRÉREQUIS ET OUTILS

DIAPOSITIVE 14 — PRÉREQUIS ET OUTILS

EXPLICATION TECHNIQUE
Faire un diagnostic rapide : demander la forme de AB lorsque A est de taille 4 × 3 et B de taille 3 × 2, puis la dérivée de log(1 + exp(z)). Le cours introduit PyTorch en parallèle des équations ; la bibliothèque ne remplace pas la compréhension des gradients. Les cinq notebooks sont autonomes et leur configuration de référence utilise le CPU. Prévoir un environnement Python 3.12 avec les dépendances du fichier requirements.txt. Une première exécution ne nécessite aucun téléchargement de données : digits est fourni par scikit-learn et les séquences sont synthétiques.

QUESTION À POSER
Quelle est la dérivée de log(1 + exp(z)) ?

RÉPONSE ATTENDUE
La sigmoïde : exp(z)/(1+exp(z)).

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 15. CONVENTIONS DE NOTATION

DIAPOSITIVE 15 — CONVENTIONS DE NOTATION

EXPLICATION TECHNIQUE
Fixer les conventions dès le début évite la plupart des erreurs de transposition. Dans les dérivations portant sur un exemple, x et les activations sont des vecteurs colonnes ; W transforme une dimension d'entrée en une dimension de sortie. Dans les implémentations, le premier axe est le batch et chaque exemple est une ligne. La même transformation devient donc X W transposée. B désigne la taille du batch, n la longueur d'une séquence, d sa largeur, C le nombre de canaux et K le nombre de classes. Le symbole élément par élément est le produit de Hadamard.

ÉQUATION — SOURCE LATEX
\begin{aligned}x&\in\mathbb{R}^{d},\quad W_\ell\in\mathbb{R}^{d_\ell\times d_{\ell-1}}\\X&\in\mathbb{R}^{B\times d},\quad H_\ell=\phi(XW_\ell^\top+\mathbf{1}b_\ell^\top)\end{aligned}

LECTURE À VOIX HAUTE
« x appartient à l’espace des vecteurs réels de dimension d. W indice ell appartient à l’espace des matrices réelles à d ell lignes et d ell moins un colonnes. »
« Grand X contient B lignes et d colonnes. H ell vaut phi appliquée à X fois W ell transposée, plus le vecteur de uns fois b ell transposé. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\in,\ \mathbb R^d` | « appartient à ; R puissance d » | Appartenance à l’espace des vecteurs réels à d composantes. |
| `x,\ X` | « x minuscule, grand x » | Un exemple sous forme de vecteur colonne, puis un batch stocké en lignes. |
| `B,\ d` | « bé, dé » | Nombre d’exemples dans le batch et dimension des entrées. |
| `\ell,\ \ell-1` | « ell, ell moins un » | Indices de la couche courante et de la couche précédente. |
| `d_\ell,\ d_{\ell-1}` | « d indice ell, d indice ell moins un » | Largeurs de sortie et d’entrée de la couche. |
| `W_\ell,\ b_\ell` | « w indice ell, b indice ell » | Matrice de poids et vecteur de biais. |
| `\mathbb R^{m\times n}` | « matrices réelles à m lignes et n colonnes » | Le signe fois sépare ici des dimensions. |
| `{}^\top` | « transposé, ou transposée » | Échange des lignes et des colonnes. |
| `\mathbf1` | « vecteur de uns » | Vecteur colonne à B composantes, utilisé pour répéter le biais. |
| `H_\ell,\ \phi` | « h indice ell, phi » | Activations du batch après application de la fonction non linéaire, composante par composante. |

INTERPRÉTATION
Pour cette couche, les colonnes de X doivent correspondre à d ell moins un. Le produit X W transposée donne B par d ell et le biais s’ajoute à chacune des B lignes.

POINT D’ATTENTION
La juxtaposition X W transposée est un produit matriciel. Le T en exposant représente une transposition, pas une puissance.

QUESTION À POSER
Pourquoi W est-il transposé dans la version batch ?

RÉPONSE ATTENDUE
Parce que les exemples sont stockés en lignes, alors que la dérivation utilise des colonnes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 16. RÉSEAUX PROFONDS

DIAPOSITIVE 16 — RÉSEAUX PROFONDS

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Relier les notions de la journée aux représentations et à la boucle d’apprentissage vues en introduction. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 17. JOUR 1 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Introduction | Histoire, comparaison ML / DL et prérequis | 65
Modélisation | MLP, activations et fonctions de perte | 80
Dérivations | Règle de la chaîne et gradients vectorisés | 75
TP 01 | MLP NumPy, gradient numérique et généralisation | 150
Restitution | Autograd, exercices et synthèse | 50

DIAPOSITIVE 17 — JOUR 1 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total. L’introduction de 65 minutes comprend environ 35 à 40 minutes pour les repères historiques et la comparaison ML / DL, puis le diagnostic des prérequis, la notation et la formulation du problème. Les 150 minutes du TP restent inchangées. Les autres séquences durent 80, 75 et 50 minutes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 18. APPRENDRE DES REPRÉSENTATIONS

DIAPOSITIVE 18 — APPRENDRE DES REPRÉSENTATIONS

EXPLICATION TECHNIQUE
Partir d'un exemple de vision : les valeurs des pixels ne sont pas directement les catégories recherchées. Le réseau ajuste plusieurs transformations pour rendre la décision finale plus simple. Éviter l'affirmation systématique selon laquelle une couche représente des contours puis des objets : c'est une intuition possible, pas une garantie pour tous les modèles. Une représentation dépend des données, de la perte et des contraintes d'architecture. Comparer largeur et profondeur : augmenter l'une ou l'autre modifie la capacité, mais aussi l'optimisation et le coût. La qualité se juge sur des données distinctes.

ÉQUATION — SOURCE LATEX
f_\theta=f_L\circ f_{L-1}\circ\cdots\circ f_1

LECTURE À VOIX HAUTE
« f paramétrée par thêta est la composée de f grand L, f grand L moins un, et ainsi de suite jusqu’à f un. On applique f un en premier. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `f_\theta` | « f paramétrée par thêta » | Fonction calculée par le réseau complet. |
| `\theta` | « thêta » | Ensemble des paramètres du réseau. |
| `L` | « grand ell » | Nombre de transformations dans la composition. |
| `f_1,\ f_{L-1},\ f_L` | « f un, f grand ell moins un, f grand ell » | Première transformation, avant-dernière et dernière. |
| `\circ` | « rond, ou composée avec » | Composition de fonctions. La fonction à droite agit d’abord. |
| `\cdots` | « et ainsi de suite » | Transformations intermédiaires omises pour alléger l’écriture. |

INTERPRÉTATION
Le résultat d’une couche devient l’entrée de la suivante.

POINT D’ATTENTION
Le rond de composition n’est ni une multiplication ordinaire ni un produit terme à terme.

QUESTION À POSER
Une architecture plus profonde est-elle toujours meilleure ?

RÉPONSE ATTENDUE
Non : capacité, optimisation, données disponibles et biais inductif interagissent.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

## 19. LE NEURONE DIFFÉRENTIABLE

DIAPOSITIVE 19 — LE NEURONE DIFFÉRENTIABLE

EXPLICATION TECHNIQUE
Distinguer le perceptron historique à seuil d'un neurone entraîné par gradient. Une fonction seuil n'a pas la dérivée utile souhaitée ; les réseaux modernes emploient des activations différentiables presque partout ou des conventions de sous-gradient. Le biais déplace la frontière sans imposer qu'elle passe par l'origine. Les poids ne sont pas des importances universelles : leur interprétation dépend de l'échelle des variables et des couches suivantes. Faire calculer z pour x=(2,-1), w=(0,5;1) et b=1 : z=1, puis appliquer une ReLU pour obtenir 1.

ÉQUATION — SOURCE LATEX
z=w^\top x+b,\qquad a=\phi(z)

LECTURE À VOIX HAUTE
« z vaut w transposé fois x, plus b. a vaut phi de z. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `x` | « x » | Vecteur d’entrée à d composantes. |
| `w,\ w^\top` | « w, w transposé » | Vecteur de poids puis sa transposée. |
| `w^\top x` | « produit scalaire de w et x » | Somme des produits des composantes correspondantes. |
| `b` | « bé » | Biais scalaire ajouté au produit scalaire. |
| `z` | « zède » | Préactivation scalaire, avant la non-linéarité. |
| `\phi` | « phi » | Fonction d’activation. |
| `a=\phi(z)` | « a égale phi de zède » | Sortie du neurone après activation. |

INTERPRÉTATION
Le neurone combine les entrées par un calcul affine puis applique une non-linéarité.

POINT D’ATTENTION
w transposé fois x est un scalaire. Phi de z se lit comme l’application d’une fonction, pas comme phi multiplié par z.

QUESTION À POSER
Combien de paramètres pour une entrée de dimension d ?

RÉPONSE ATTENDUE
d poids et un biais, soit d+1.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 20. POURQUOI LA NON-LINÉARITÉ ?

DIAPOSITIVE 20 — POURQUOI LA NON-LINÉARITÉ ?

EXPLICATION TECHNIQUE
Développer le produit au tableau pour montrer exactement ce que l'empilement affine peut exprimer. On peut absorber deux couches dans une seule matrice et un seul biais. La représentation du XOR constitue un contre-exemple classique à une séparation linéaire dans l'espace d'entrée : ses classes occupent des coins opposés. Une couche cachée non linéaire transforme cet espace. Ne pas confondre ce constat avec les effets d'une factorisation linéaire sur l'optimisation ; ici, on parle de la classe de fonctions représentables, pas de la trajectoire suivie pendant l'entraînement.

ÉQUATION — SOURCE LATEX
W_2(W_1x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2)

LECTURE À VOIX HAUTE
« W deux appliqué à W un fois x plus b un, puis plus b deux, vaut W deux fois W un appliqué à x, plus W deux fois b un plus b deux. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `x` | « x » | Vecteur d’entrée. |
| `W_1,\ W_2` | « w un, w deux » | Matrices de la première et de la deuxième couche affine. |
| `b_1,\ b_2` | « b un, b deux » | Vecteurs de biais des deux couches. |
| `W_2W_1` | « w deux fois w un » | Matrice composée. L’ordre des facteurs compte. |
| `W_2b_1+b_2` | « w deux fois b un, plus b deux » | Biais total obtenu après développement. |
| `(\cdot)` | « parenthèses » | Regroupent un calcul à effectuer comme un tout. |
| `=` | « égale » | Les deux expressions calculent exactement la même fonction. |

INTERPRÉTATION
Deux couches affines successives peuvent se remplacer par une seule couche affine.

POINT D’ATTENTION
On utilise la distributivité et l’associativité. On ne permute pas les matrices : W deux W un est généralement différent de W un W deux.

QUESTION À POSER
Que devient un réseau de dix couches linéaires ?

RÉPONSE ATTENDUE
Une application affine unique, si des biais sont présents.

LECTURES ET RÉFÉRENCES
Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

## 21. ACTIVATIONS : VALEURS ET SATURATION

DIAPOSITIVE 21 — ACTIVATIONS : VALEURS ET SATURATION

EXPLICATION TECHNIQUE
Lire les deux courbes comme des fonctions scalaires appliquées composante par composante. La sigmoïde est utile pour une probabilité binaire en sortie ; dans des couches cachées profondes, sa saturation peut réduire fortement les gradients. ReLU évite la saturation sur la branche positive mais peut laisser certaines unités inactives pour tous les exemples. Une activation n'est donc pas choisie seulement pour son coût : il faut considérer l'initialisation et la distribution des préactivations. Les courbes présentées sont calculées directement à partir des définitions, sans mesures d'entraînement.

QUESTION À POSER
Quelle est la valeur de la sigmoïde en zéro ?

RÉPONSE ATTENDUE
0,5 ; sa dérivée en zéro vaut 0,25.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 22. DÉRIVÉES DES ACTIVATIONS

DIAPOSITIVE 22 — DÉRIVÉES DES ACTIVATIONS

EXPLICATION TECHNIQUE
Retrouver la dérivée de la sigmoïde par la dérivation d'un inverse et d'une exponentielle. Son maximum est 1/4, ce qui prépare l'analyse de l'atténuation des gradients, sans suffire à elle seule à décrire un réseau complet : les matrices de poids interviennent aussi. Pour ReLU, la dérivée n'existe pas au point zéro ; la valeur zéro utilisée dans nos calculs est une convention pratique. Φ est la fonction de répartition de la loi normale centrée réduite. GELU ne doit pas être confondue avec une probabilité de sortie : c'est une activation.

ÉQUATION — SOURCE LATEX
\sigma'(z)=\sigma(z)(1-\sigma(z)),\quad\phi_{\rm ReLU}'(z)=\mathbf{1}_{z>0}\\\operatorname{GELU}(z)=z\Phi(z)

LECTURE À VOIX HAUTE
« Sigma prime de z vaut sigma de z fois un moins sigma de z. »
« La dérivée de ReLU en z vaut l’indicatrice de z strictement positif, pour z différent de zéro. »
« GELU de z vaut z fois grand phi de z. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `z` | « zède » | Préactivation scalaire. |
| `\sigma(z)` | « sigma de zède » | Sigmoïde logistique. |
| `{}'` | « prime » | Dérivée d’une fonction scalaire par rapport à son argument. |
| `\sigma'(z)` | « sigma prime de zède » | Dérivée de la sigmoïde au point z. |
| `\phi_{\rm ReLU}` | « phi indice rélu » | Fonction ReLU : maximum entre zéro et z. |
| `\mathbf1_{z>0}` | « indicatrice de zède strictement positif » | Vaut un si z est positif et zéro sinon. |
| `\Phi(z)` | « grand phi de zède » | Fonction de répartition de la loi normale centrée réduite. |
| `\operatorname{GELU}(z)` | « gélu de zède » | Activation obtenue ici par z multiplié par la probabilité Phi de z. |

INTERPRÉTATION
Les dérivées déterminent comment le signal de gradient traverse les activations.

POINT D’ATTENTION
La dérivée de ReLU n’existe pas en zéro. Mettre zéro à cet endroit est une convention de calcul. Sigma, phi et grand Phi désignent trois fonctions différentes.

QUESTION À POSER
La dérivée de ReLU vaut-elle 1 pour toute entrée ?

RÉPONSE ATTENDUE
Non : elle vaut zéro sur les entrées négatives.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 23. UNE COUCHE DENSE : FORMES ET CALCUL

DIAPOSITIVE 23 — UNE COUCHE DENSE : FORMES ET CALCUL

EXPLICATION TECHNIQUE
Écrire la forme de chaque objet : a précédent a d précédent composantes, W a d courant lignes et d précédent colonnes, b a d courant composantes. Le comptage inclut exactement un biais par neurone de sortie. Pour 784 entrées et 128 unités, la couche contient 784 × 128 + 128 = 100480 paramètres. Le nombre de paramètres ne dépend pas de B, même si la mémoire des activations et le coût du calcul en dépendent. Dans PyTorch, nn.Linear(in_features, out_features) stocke précisément une matrice out_features × in_features.

ÉQUATION — SOURCE LATEX
a_\ell=\phi_\ell(W_\ell a_{\ell-1}+b_\ell),\qquad P_\ell=d_\ell(d_{\ell-1}+1)

LECTURE À VOIX HAUTE
« a indice ell vaut phi indice ell appliquée à W ell fois a ell moins un, plus b ell. »
« Le nombre P ell de paramètres vaut d ell fois la quantité d ell moins un plus un. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\ell,\ \ell-1` | « ell, ell moins un » | Numéros des couches courante et précédente. |
| `a_{\ell-1},\ a_\ell` | « a indice ell moins un, a indice ell » | Entrée et sortie de la couche. |
| `W_\ell` | « w indice ell » | Matrice à d ell lignes et d ell moins un colonnes. |
| `b_\ell` | « b indice ell » | Un biais par neurone de sortie. |
| `\phi_\ell` | « phi indice ell » | Activation appliquée à chaque préactivation. |
| `P_\ell` | « pé indice ell » | Nombre total de poids et de biais de la couche. |
| `d_\ell(d_{\ell-1}+1)` | « d ell fois, entre parenthèses, d ell moins un plus un » | Chaque sortie utilise d ell moins un poids et un biais. |

INTERPRÉTATION
La formule de calcul et la formule de comptage décrivent la même couche dense.

POINT D’ATTENTION
Dans l’indice d ell moins un, « moins un » fait partie du numéro de couche. Ce n’est pas la largeur d ell diminuée de un.

QUESTION À POSER
Une couche 64 → 10 contient combien de paramètres ?

RÉPONSE ATTENDUE
64×10+10 = 650.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 24. MLP : ARCHITECTURE ET PARAMÈTRES

Opération | Forme pour un batch B | Paramètres
Entrée | B × 2 | 0
Dense + ReLU | B × 16 | 2×16 + 16 = 48
Dense : logits | B × 2 | 16×2 + 2 = 34
Softmax pour lecture | B × 2 | 0
Total | 2 classes | 82

DIAPOSITIVE 24 — MLP : ARCHITECTURE ET PARAMÈTRES

EXPLICATION TECHNIQUE
Effectuer le comptage couche par couche, puis la somme. Pour l'exemple 2 → 16 → 2, la première couche comporte 32 poids et 16 biais ; la seconde 32 poids et 2 biais. Le réseau a donc 82 paramètres entraînables. Les activations ne portent pas de paramètres pour une ReLU ou une sigmoïde standard. Cette architecture sera utilisée dans le premier TP sur deux lunes. L'objectif est de relier les dimensions du code à une décision géométrique dans un espace de dimension deux, où le problème peut être visualisé sans réduction de dimension.

QUESTION À POSER
Changer le batch de 32 à 64 double-t-il les paramètres ?

RÉPONSE ATTENDUE
Non. Cela augmente le nombre d’activations conservées pendant le calcul.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 25. PERTE DE RÉGRESSION

DIAPOSITIVE 25 — PERTE DE RÉGRESSION

EXPLICATION TECHNIQUE
Développer la somme des carrés composante par composante. Le gradient a la même dimension que la sortie. Si le modèle surestime y, le signe du gradient est positif et une descente réduit la prédiction localement. Sous une hypothèse de bruit gaussien de variance constante, la minimisation des carrés a une interprétation de maximum de vraisemblance ; cette hypothèse n'est pas universelle. Certains logiciels divisent aussi par le nombre de composantes de sortie. Il faut donc vérifier la réduction utilisée avant de comparer une dérivation et les gradients d'une bibliothèque.

ÉQUATION — SOURCE LATEX
\ell(\hat y,y)=\frac12\|\hat y-y\|_2^2,\qquad\nabla_{\hat y}\ell=\hat y-y

LECTURE À VOIX HAUTE
« La perte de y chapeau et y vaut un demi de la norme deux de leur différence, au carré. »
« Le gradient de ell par rapport à y chapeau vaut y chapeau moins y. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\ell` | « ell minuscule » | Fonction de perte. |
| `\hat y` | « y chapeau » | Prédiction du modèle, scalaire ou vecteur. |
| `y` | « y » | Valeur cible attendue. |
| `\frac12` | « un demi » | Facteur qui simplifie la dérivée du carré. |
| `\hat y-y` | « y chapeau moins y » | Écart entre la prédiction et la cible. |
| `\\|\hat y-y\\|_2` | « norme deux de y chapeau moins y » | Longueur euclidienne du vecteur des écarts. Les doubles barres désignent une norme et le deux en indice indique son type. |
| `{}^2` | « au carré » | On élève la norme entière au carré, ce qui donne la somme des carrés des écarts. |
| `\nabla` | « nabla » | Notation d’un gradient. |
| `\nabla_{\hat y}\ell` | « gradient de ell par rapport à y chapeau » | Vecteur des dérivées partielles de la perte par rapport aux composantes de la prédiction. |

INTERPRÉTATION
Le carré pénalise les écarts dans les deux sens. Par exemple, pour une sortie scalaire y chapeau égale trois et y égale un, la perte vaut deux et le gradient vaut deux.

POINT D’ATTENTION
La cible y reste fixée pendant cette dérivation. Le gradient pointe localement vers l’augmentation de la perte. La descente utilise son opposé. Une moyenne sur les composantes ajouterait un facteur de normalisation.

QUESTION À POSER
Quel gradient obtient-on pour y=2 et une prédiction 5 ?

RÉPONSE ATTENDUE
3 avec la convention de cette diapositive.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 26. CLASSIFICATION : SOFTMAX ET ENTROPIE CROISÉE

DIAPOSITIVE 26 — CLASSIFICATION : SOFTMAX ET ENTROPIE CROISÉE

EXPLICATION TECHNIQUE
Pour une cible one-hot, un seul terme de la somme reste : moins le logarithme de la probabilité attribuée à la classe correcte. Deux sorties très différentes peuvent conduire à la même classe prédite mais à des pertes différentes, ce qui permet à l'optimiseur d'exploiter la confiance relative. Les probabilités produites ne sont pas automatiquement calibrées. Distinguer classification exclusive avec softmax et classification multi-label avec des sigmoïdes indépendantes. Les équations ci-dessus concernent des classes mutuellement exclusives et une distribution cible de somme un.

ÉQUATION — SOURCE LATEX
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}},\qquad\ell(z,y)=-\sum_{k=1}^{K}y_k\log p_k

LECTURE À VOIX HAUTE
« p indice k vaut l’exponentielle du logit z k, divisée par la somme des exponentielles de tous les logits. »
« La perte de z et y vaut moins la somme, pour k de un à grand K, de y k fois le logarithme de p k. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `z,\ z_k` | « zède, zède indice k » | Vecteur des logits et score brut de la classe k. |
| `e^{z_k}` | « exponentielle de zède indice k » | Transforme un score en quantité strictement positive. |
| `p_k` | « pé indice k » | Probabilité prédite pour la classe k après softmax. |
| `\sum_j e^{z_j}` | « somme sur j des exponentielles de z j » | Normalisation calculée sur toutes les classes. |
| `K,\ k,\ j` | « grand k, k, j » | Nombre de classes et indices qui parcourent les classes. |
| `y_k` | « y indice k » | Composante de la cible. En one-hot, elle vaut un pour la classe correcte et zéro ailleurs. |
| `\log p_k` | « logarithme de pé indice k » | Logarithme naturel de la probabilité prédite. |
| `-\sum_{k=1}^K y_k\log p_k` | « moins la somme des y k logarithme de p k » | Entropie croisée entre la cible et la distribution prédite. |
| `\ell(z,y)` | « ell de zède et y » | Perte scalaire associée aux logits et à la cible. |

INTERPRÉTATION
Avec une cible one-hot de classe c, la perte devient moins le logarithme de la probabilité de c.

POINT D’ATTENTION
La perte reçoit ici des logits z. Il ne faut pas appliquer deux fois softmax si la fonction de bibliothèque le calcule déjà.

QUESTION À POSER
Pourquoi accuracy et entropie croisée ne racontent-elles pas la même chose ?

RÉPONSE ATTENDUE
L’accuracy ne dépend que de l’argmax ; la perte dépend des probabilités.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — CrossEntropyLoss
https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html

## 27. STABILITÉ NUMÉRIQUE DES LOGITS

DIAPOSITIVE 27 — STABILITÉ NUMÉRIQUE DES LOGITS

EXPLICATION TECHNIQUE
Montrer l'invariance en multipliant numérateur et dénominateur par exp(-m). L'exemple z=(1000,1001) provoque un débordement si l'on calcule les exponentielles naïvement ; après translation, les arguments deviennent -1 et 0. En PyTorch, appliquer softmax avant CrossEntropyLoss change l'objet donné à la perte, qui attend déjà des logits et applique sa propre normalisation stable. Pour une classification binaire à une sortie, la version analogue est BCEWithLogitsLoss. La précision numérique est une contrainte d'implémentation qui doit être distinguée de la définition mathématique.

ÉQUATION — SOURCE LATEX
\ell(z,c)=-z_c+m+\log\sum_j e^{z_j-m},\qquad m=\max_j z_j

LECTURE À VOIX HAUTE
« La perte de z et de la classe c vaut moins z indice c, plus m, plus le logarithme de la somme des exponentielles de z j moins m. »
« m est le maximum des logits z j. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `z_j,\ z_c` | « zède indice j, zède indice c » | Score d’une classe quelconque et score de la classe correcte. |
| `c` | « cé » | Indice entier de la classe cible. |
| `m=\max_j z_j` | « m égale le maximum, sur j, de z j » | Plus grand logit de l’exemple. |
| `e^{z_j-m}` | « exponentielle de z j moins m » | Exponentielle d’un score décalé, dont l’exposant est inférieur ou égal à zéro. |
| `\sum_j` | « somme sur j » | Somme sur toutes les classes. |
| `\log` | « logarithme » | Logarithme naturel. |
| `\ell(z,c)` | « ell de zède et cé » | Entropie croisée calculée avec la classe cible c. |

INTERPRÉTATION
Soustraire le maximum avant l’exponentielle évite les très grandes exponentielles tout en conservant la même perte mathématique.

POINT D’ATTENTION
Le m ajouté hors du logarithme compense le décalage. Le calcul stabilisé ne consiste pas à supprimer le terme m.

QUESTION À POSER
Faut-il appliquer softmax avant CrossEntropyLoss ?

RÉPONSE ATTENDUE
Non : fournir les logits et des étiquettes entières dans notre configuration.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — CrossEntropyLoss
https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html

## 28. RISQUE EMPIRIQUE ET GÉNÉRALISATION

DIAPOSITIVE 28 — RISQUE EMPIRIQUE ET GÉNÉRALISATION

EXPLICATION TECHNIQUE
La fonction minimisée est une approximation du risque attendu sur de nouvelles données. Une faible erreur empirique ne suffit donc pas : le modèle peut mémoriser le bruit ou exploiter une fuite d'information. Le symbole approximation rappelle qu'un réseau non convexe est généralement optimisé par un nombre fini de mises à jour sans garantie d'atteindre un minimum global. Expliquer le rôle de chaque partition et insister sur l'apprentissage du prétraitement à partir du train seul. Une augmentation de données doit respecter la sémantique de la cible et ne jamais relier les partitions.

ÉQUATION — SOURCE LATEX
\hat R(\theta)=\frac1N\sum_{i=1}^{N}\ell(f_\theta(x_i),y_i),\qquad\hat\theta\approx\arg\min_\theta\hat R(\theta)

LECTURE À VOIX HAUTE
« R chapeau de thêta vaut un sur grand N fois la somme des pertes sur les N exemples. »
« Thêta chapeau est approximativement un argument qui minimise R chapeau par rapport à thêta. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\hat R(\theta)` | « R chapeau de thêta » | Risque empirique : perte moyenne mesurée sur l’échantillon. |
| `\theta` | « thêta » | Paramètres du modèle. |
| `\hat\theta` | « thêta chapeau » | Paramètres estimés par l’apprentissage. |
| `N,\ i` | « grand n, i » | Nombre d’exemples et indice d’exemple. |
| `x_i,\ y_i` | « x i, y i » | Entrée et cible du i-ième exemple. |
| `f_\theta(x_i)` | « f thêta de x i » | Prédiction pour cet exemple. |
| `\ell` | « ell » | Fonction de perte d’un exemple. |
| `\frac1N\sum_{i=1}^N` | « un sur N fois la somme de i égale un à N » | Moyenne arithmétique des pertes. |
| `\arg\min_\theta` | « argument du minimum par rapport à thêta » | Paramètres qui minimisent la fonction, plutôt que valeur minimale de cette fonction. |
| `\approx` | « est approximativement égal à » | L’optimisation numérique ne garantit pas ici un minimum global exact. |

INTERPRÉTATION
L’apprentissage cherche des paramètres qui rendent faible la perte moyenne d’entraînement.

POINT D’ATTENTION
Le chapeau de R rappelle l’estimation à partir d’un échantillon. Un faible risque empirique ne suffit pas à établir un faible risque sur de nouvelles données.

QUESTION À POSER
Où choisit-on le nombre d’époques ?

RÉPONSE ATTENDUE
À partir du train et de la validation, jamais du test.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

Geoffrey Daniel — Réseaux de neurones et deep learning : utilisation et méthodologie
https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf

## 29. DESCENTE DE GRADIENT

DIAPOSITIVE 29 — DESCENTE DE GRADIENT

EXPLICATION TECHNIQUE
Faire dériver un risque quadratique simple avant de parler de réseau. La rétropropagation calcule les dérivées ; SGD ou Adam utilisent ces dérivées pour choisir une mise à jour. Un pas trop grand peut augmenter la perte même si le gradient est correct. Un pas trop petit peut rendre la progression indétectable au budget disponible. Le sens de descente est une propriété locale à l'ordre un et ne constitue pas une preuve d'amélioration pour un pas fini. Les conditions théoriques de convergence dépendent de la régularité de la fonction et de la suite des pas.

ÉQUATION — SOURCE LATEX
\theta_{t+1}=\theta_t-\eta_t\nabla_\theta\hat R(\theta_t)

LECTURE À VOIX HAUTE
« Thêta à l’itération t plus un vaut thêta à l’itération t, moins êta t fois le gradient, par rapport à thêta, du risque empirique évalué en thêta t. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `t,\ t+1` | « té, té plus un » | Itération courante et itération suivante. |
| `\theta_t,\ \theta_{t+1}` | « thêta indice t, thêta indice t plus un » | Paramètres avant et après la mise à jour. |
| `\eta_t` | « êta indice t » | Taux d’apprentissage, positif, éventuellement variable selon l’itération. |
| `\nabla_\theta` | « gradient par rapport à thêta » | Vecteur des dérivées partielles selon les paramètres. |
| `\hat R(\theta_t)` | « R chapeau évalué en thêta t » | Risque empirique au point courant. |
| `-\eta_t\nabla_\theta\hat R(\theta_t)` | « moins êta t fois le gradient du risque » | Déplacement choisi dans la direction opposée au gradient. |

INTERPRÉTATION
Le gradient indique une direction d’augmentation locale. Le signe moins choisit la direction de descente.

POINT D’ATTENTION
Le gradient doit être évalué aux paramètres courants. Un pas trop grand peut augmenter la perte malgré le signe moins.

QUESTION À POSER
Un gradient correct garantit-il que chaque étape diminue la perte ?

RÉPONSE ATTENDUE
Non : le pas et l’approximation stochastique interviennent.

LECTURES ET RÉFÉRENCES
Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

## 30. RÈGLE DE LA CHAÎNE

DIAPOSITIVE 30 — RÈGLE DE LA CHAÎNE

EXPLICATION TECHNIQUE
Dessiner au tableau le graphe d'un calcul scalaire, puis identifier la valeur transportée vers l'avant et la sensibilité transportée vers l'arrière. Le gradient arrière d'un nœud est la variation de la perte due à une petite variation de ce nœud. Si une variable intervient dans plusieurs opérations, toutes ses contributions doivent être additionnées. C'est ce qui rend nécessaire l'accumulation, en particulier dans les connexions résiduelles et le partage de paramètres. On ne calcule pas un gradient différent pour chaque branche puis on n'en conserve qu'un seul.

ÉQUATION — SOURCE LATEX
z=g(x),\quad u=h(z),\quad \frac{\partial\ell}{\partial x}=\frac{\partial\ell}{\partial u}\frac{\partial u}{\partial z}\frac{\partial z}{\partial x}

LECTURE À VOIX HAUTE
« z vaut g de x et u vaut h de z. »
« La dérivée partielle de ell par rapport à x vaut la dérivée de ell par rapport à u, fois la dérivée de u par rapport à z, fois la dérivée de z par rapport à x. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `x,\ z,\ u` | « x, zède, u » | Variables scalaires successives du calcul. |
| `g,\ h` | « gé, ache » | Fonctions qui relient ces variables. |
| `\ell` | « ell » | Perte scalaire finale. |
| `\partial` | « dérivée partielle, ou d rond » | Symbole de dérivation en faisant varier une variable et en fixant les autres variables indépendantes. |
| `\frac{\partial\ell}{\partial x}` | « dérivée partielle de ell par rapport à x » | Sensibilité finale recherchée. |
| `\frac{\partial\ell}{\partial u},\ \frac{\partial u}{\partial z},\ \frac{\partial z}{\partial x}` | « dérivées de ell selon u, de u selon z et de z selon x » | Sensibilités locales le long de la chaîne. |
| `\frac{\partial\ell}{\partial u}\frac{\partial u}{\partial z}\frac{\partial z}{\partial x}` | « produit des trois dérivées locales » | Propagation de la sensibilité finale à travers les opérations intermédiaires. |

INTERPRÉTATION
Une petite variation de x modifie z, puis u, puis la perte. Le produit combine ces effets.

POINT D’ATTENTION
La diapositive traite une chaîne scalaire. Pour des vecteurs, il faut des jacobiennes et des conventions de dimensions. Sur plusieurs chemins, on additionne les contributions.

QUESTION À POSER
Que fait-on si un paramètre est utilisé deux fois dans le graphe ?

RÉPONSE ATTENDUE
On somme les contributions de ses deux utilisations.

LECTURES ET RÉFÉRENCES
Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

## 31. EXEMPLE SCALAIRE : UN PAS COMPLET

DIAPOSITIVE 31 — EXEMPLE SCALAIRE : UN PAS COMPLET

EXPLICATION TECHNIQUE
Calculer d'abord z=1, puis a=1/(1+exp(-1)). Le résidu est négatif car la sortie est inférieure à la cible. Sa multiplication par la dérivée de la sigmoïde, puis par x, donne un gradient d'environ -0,10575. Pour le biais, le même calcul omet le facteur x et donne environ -0,05288. La mise à jour produit w≈0,51058 et b≈0,00529. Recalculer ensuite la perte et vérifier qu'elle diminue pour ce pas précis. Cet exemple concerne une sigmoïde associée à une perte quadratique, et non la simplification softmax-entropie croisée présentée ensuite.

ÉQUATION — SOURCE LATEX
\ell=\tfrac12(a-y)^2,\quad a=\sigma(wx+b)\\\frac{\partial\ell}{\partial w}=(a-y)a(1-a)x\approx-0.1058

LECTURE À VOIX HAUTE
« Ell vaut un demi de a moins y, au carré. a vaut la sigmoïde de w fois x plus b. »
« La dérivée de ell par rapport à w vaut a moins y, fois a, fois un moins a, fois x. Elle vaut ici environ moins zéro virgule un zéro cinq huit. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\ell` | « ell » | Perte quadratique scalaire. |
| `a,\ y` | « a, y » | Prédiction du neurone et cible. |
| `\tfrac12(a-y)^2` | « un demi de a moins y au carré » | Carré de l’erreur, multiplié par un demi. |
| `x,\ w,\ b` | « x, w, bé » | Entrée scalaire, poids et biais. |
| `\sigma(wx+b)` | « sigma de w x plus b » | Sigmoïde de la préactivation. |
| `\frac{\partial\ell}{\partial w}` | « dérivée partielle de ell par rapport à w » | Variation locale de la perte quand seul le poids varie. |
| `a(1-a)` | « a fois un moins a » | Dérivée de la sigmoïde exprimée à partir de sa sortie. |
| `(a-y)a(1-a)x` | « a moins y, fois a, fois un moins a, fois x » | Produit des trois facteurs de la règle de la chaîne. |
| `\approx-0.1058` | « environ moins zéro virgule un zéro cinq huit » | Valeur arrondie du gradient dans l’exemple. |

INTERPRÉTATION
Les trois facteurs sont la dérivée de la perte selon a, celle de a selon la préactivation et celle de la préactivation selon w.

POINT D’ATTENTION
Le gradient négatif entraîne une augmentation de w lors d’une descente. Il ne signifie pas que la perte est négative.

QUESTION À POSER
Quel facteur disparaît dans la dérivée par rapport au biais ?

RÉPONSE ATTENDUE
Le facteur x ; la dérivée de wx+b par rapport à b vaut 1.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 32. GRADIENT DE SOFTMAX + ENTROPIE CROISÉE

DIAPOSITIVE 32 — GRADIENT DE SOFTMAX + ENTROPIE CROISÉE

EXPLICATION TECHNIQUE
Développer moins la somme y_i log(p_i), puis appliquer la dérivée de chaque p_i par rapport à z_j. La somme des y_i vaut un ; on obtient p_j-y_j. Pour la bonne classe, le gradient est négatif tant que la probabilité n'atteint pas un ; pour les autres classes, il est positif. La somme des composantes du gradient vaut zéro, conformément à l'invariance de softmax à l'ajout d'une constante. Avec une moyenne sur B exemples, le facteur 1/B doit être appliqué une fois, soit ici soit dans l'agrégation, pas deux fois.

ÉQUATION — SOURCE LATEX
\frac{\partial p_i}{\partial z_j}=p_i(\delta_{ij}-p_j),\qquad\frac{\partial\ell}{\partial z}=p-y

LECTURE À VOIX HAUTE
« La dérivée de p i par rapport à z j vaut p i fois delta i j moins p j. »
« Le gradient de ell par rapport au vecteur z vaut p moins y. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `p_i,\ p_j` | « pé indice i, pé indice j » | Probabilités de deux classes après softmax. |
| `z_j` | « zède indice j » | Logit de la classe j. |
| `\frac{\partial p_i}{\partial z_j}` | « dérivée de pé i par rapport à zède j » | Une entrée de la jacobienne de softmax. |
| `\delta_{ij}` | « delta de Kronecker, indices i j » | Vaut un si i égale j et zéro sinon. |
| `\ell` | « ell » | Entropie croisée pour un exemple. |
| `\frac{\partial\ell}{\partial z}` | « gradient de ell par rapport à zède » | Vecteur des dérivées par rapport à tous les logits. |
| `p-y` | « pé moins y » | Différence composante par composante entre distribution prédite et cible. |
| `i,\ j` | « i, j » | Indices de classes. |

INTERPRÉTATION
La combinaison softmax et entropie croisée conduit à un gradient simple malgré les dépendances entre toutes les classes.

POINT D’ATTENTION
La cible doit sommer à un pour cette simplification. Delta i j est ici une indicatrice, alors que delta ell désignera un signal de gradient dans les couches.

QUESTION À POSER
Pourquoi les gradients des logits somment-ils à zéro ?

RÉPONSE ATTENDUE
Parce que les distributions p et y ont toutes deux une somme égale à un.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 33. RÉTROPROPAGATION D’UNE COUCHE DENSE

DIAPOSITIVE 33 — RÉTROPROPAGATION D’UNE COUCHE DENSE

EXPLICATION TECHNIQUE
Vérifier les dimensions avant de développer la dérivée. δ a d courant composantes et a précédent en a d précédent ; leur produit extérieur donne bien une matrice de même forme que W. Pour une composante W_ij, la sensibilité de z_i est a_j et celle de la perte par rapport à z_i est δ_i. Le biais est ajouté directement à z, d'où son gradient δ. Ces formules concernent un exemple unique. Le passage au batch se fait ensuite en additionnant ou en moyennant les contributions selon la réduction de la perte.

ÉQUATION — SOURCE LATEX
\delta_\ell=\frac{\partial\ell}{\partial z_\ell},\quad\nabla_{W_\ell}\ell=\delta_\ell a_{\ell-1}^{\top}\\\nabla_{b_\ell}\ell=\delta_\ell,\quad\frac{\partial\ell}{\partial a_{\ell-1}}=W_\ell^\top\delta_\ell

LECTURE À VOIX HAUTE
« Delta ell est le gradient de la perte par rapport à la préactivation z ell. »
« Le gradient selon W ell vaut delta ell fois a ell moins un transposé. Le gradient selon b ell vaut delta ell. »
« Le gradient selon a ell moins un vaut W ell transposée fois delta ell. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\ell` | « ell minuscule » | Fonction de perte dans les dérivées. |
| `{}_{\ell},\ {}_{\ell-1}` | « indice ell, indice ell moins un » | Indices de couche. Le même caractère ell a ici un rôle distinct de celui de la perte. |
| `z_\ell` | « zède indice ell » | Vecteur des préactivations de la couche. |
| `\delta_\ell` | « delta indice ell » | Gradient de la perte selon les préactivations de la couche. |
| `W_\ell,\ b_\ell` | « w indice ell, b indice ell » | Matrice des poids et vecteur des biais. |
| `a_{\ell-1}` | « a indice ell moins un » | Vecteur colonne des activations d’entrée. |
| `{}^\top` | « transposé » | Échange des lignes et colonnes. |
| `\delta_\ell a_{\ell-1}^\top` | « delta ell fois a ell moins un transposé » | Produit extérieur : matrice de la même forme que W ell. |
| `\nabla_{W_\ell}\ell,\ \nabla_{b_\ell}\ell` | « gradient de ell selon W ell ; selon b ell » | Dérivées par rapport à chaque poids et à chaque biais. |
| `W_\ell^\top\delta_\ell` | « W ell transposée fois delta ell » | Gradient transmis à la couche précédente. |

INTERPRÉTATION
Chaque poids reçoit la sensibilité de son neurone de sortie multipliée par l’activation qui lui arrive.

POINT D’ATTENTION
Ces expressions concernent un exemple. Une perte moyennée sur un batch exige une réduction cohérente des contributions.

QUESTION À POSER
Pourquoi le gradient de W a-t-il la même forme que W ?

RÉPONSE ATTENDUE
Il contient une dérivée pour chacun de ses paramètres scalaires.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

## 34. PROPAGER LE SIGNAL DANS LES COUCHES CACHÉES

DIAPOSITIVE 34 — PROPAGER LE SIGNAL DANS LES COUCHES CACHÉES

EXPLICATION TECHNIQUE
La multiplication par W transposée distribue le signal d'erreur vers les unités de la couche précédente. Le produit de Hadamard filtre ensuite ce signal par la sensibilité locale de l'activation. Pour ReLU, les préactivations négatives ne transmettent aucun gradient par cette branche. Expliquer pourquoi il faut utiliser les poids du passage avant pour tout le passage arrière : mettre W à jour avant de calculer les gradients des couches précédentes mélangerait deux états du modèle. L'optimiseur intervient après que tous les gradients nécessaires ont été calculés.

ÉQUATION — SOURCE LATEX
\delta_\ell=\left(W_{\ell+1}^\top\delta_{\ell+1}\right)\odot\phi_\ell'(z_\ell)

LECTURE À VOIX HAUTE
« Delta ell vaut W ell plus un transposée fois delta ell plus un, puis ce résultat multiplié terme à terme par phi ell prime de z ell. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\delta_\ell,\ \delta_{\ell+1}` | « delta ell, delta ell plus un » | Gradients selon les préactivations de la couche courante et de la suivante. |
| `W_{\ell+1}^\top` | « W de la couche ell plus un, transposée » | Matrice qui ramène la sensibilité depuis la couche suivante. |
| `\phi_\ell'(z_\ell)` | « phi ell prime de zède ell » | Dérivée de l’activation, évaluée à chaque préactivation. |
| `\odot` | « produit de Hadamard, ou produit terme à terme » | Chaque composante est multipliée par la composante correspondante. |
| `\ell+1` | « ell plus un » | Indice de la couche suivante. |
| `z_\ell` | « zède ell » | Valeurs calculées avant l’activation lors du passage avant. |

INTERPRÉTATION
La propagation arrière combine l’effet des poids de la couche suivante et la dérivée locale de l’activation.

POINT D’ATTENTION
Le premier produit est matriciel. Le symbole cercle avec point demande ensuite un produit terme à terme, avec deux vecteurs de même taille.

QUESTION À POSER
Peut-on mettre les poids à jour pendant que l’on remonte les couches ?

RÉPONSE ATTENDUE
Pas dans la rétropropagation standard : on utilise un même état des poids.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 35. GRADIENTS VECTORISÉS SUR UN BATCH

DIAPOSITIVE 35 — GRADIENTS VECTORISÉS SUR UN BATCH

EXPLICATION TECHNIQUE
Prendre B=32, une entrée de largeur 16 et une sortie de largeur 10. H est 32×16, W est 10×16, Z et D sont 32×10. D transposée multipliée par H donne 10×16. Dans nos implémentations NumPy, D contient déjà la division par B issue de la perte moyenne ; on ne divise donc pas à nouveau le gradient des poids. Les biais sont broadcastés pendant le passage avant : le passage arrière doit inverser cette opération en sommant sur les axes répétés. Ce principe s'applique à de nombreux bugs d'autograd manuel.

ÉQUATION — SOURCE LATEX
Z=HW^\top+\mathbf1b^\top,\quad D=\frac{\partial\mathcal L}{\partial Z}\\\nabla_W\mathcal L=D^\top H,\quad\nabla_b\mathcal L=\sum_{i=1}^{B}D_{i,:},\quad\nabla_H\mathcal L=DW

LECTURE À VOIX HAUTE
« Z vaut H fois W transposée, plus le vecteur de uns fois b transposé. D est le gradient de la perte totale par rapport à Z. »
« Le gradient selon W vaut D transposée fois H. Celui selon b est la somme des lignes de D. Celui selon H vaut D fois W. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `H,\ W,\ Z` | « grand ache, w, zède » | Activations d’entrée B par d entrée, poids d sortie par d entrée, préactivations B par d sortie. |
| `B` | « bé » | Nombre d’exemples du batch. |
| `b,\ \mathbf1 b^\top` | « bé ; vecteur de uns fois b transposé » | Vecteur des biais, puis matrice qui répète ce biais sur chaque ligne. |
| `\mathcal L` | « grand ell calligraphique » | Perte agrégée sur le batch, avec une réduction définie. |
| `D=\frac{\partial\mathcal L}{\partial Z}` | « D égale le gradient de grand ell selon Z » | Matrice des sensibilités, de même forme que Z. |
| `D^\top H` | « D transposée fois H » | Gradient des poids, de même forme que W. |
| `D_{i,:}` | « ligne i de D, toutes les colonnes » | Sensibilités correspondant à l’exemple i. Le deux-points sélectionne toutes les colonnes. |
| `\sum_{i=1}^B D_{i,:}` | « somme des lignes de D, de i égale un à B » | Gradient du biais partagé entre les exemples. |
| `DW` | « D fois W » | Gradient des activations d’entrée H. |
| `\nabla` | « nabla, gradient » | Dérivées par rapport à l’objet indiqué en indice. |

INTERPRÉTATION
Les produits matriciels regroupent les calculs de chaque exemple sans changer les dérivées.

POINT D’ATTENTION
Si D contient déjà le facteur un sur B d’une perte moyenne, il ne faut pas diviser encore une fois le gradient des poids.

QUESTION À POSER
Si D=(p-y)/B, faut-il encore diviser DᵀH par B ?

RÉPONSE ATTENDUE
Non : cela réduirait le gradient d’un facteur B supplémentaire.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 36. VÉRIFIER UN GRADIENT NUMÉRIQUEMENT

DIAPOSITIVE 36 — VÉRIFIER UN GRADIENT NUMÉRIQUEMENT

EXPLICATION TECHNIQUE
Une vérification numérique est un outil de diagnostic, pas une méthode pratique d'entraînement : elle exige deux évaluations de la perte par paramètre testé. Une valeur epsilon trop grande produit une erreur de troncature ; trop petite, une erreur d'arrondi. Une plage autour de 10 puissance moins cinq convient souvent en double précision, sans être une constante universelle. Désactiver le dropout et contrôler toute source d'aléa. Si la perturbation traverse zéro pour une ReLU, les dérivées peuvent différer sans que la règle de propagation soit incorrecte. Le TP vérifie séparément chaque tableau de paramètres.

ÉQUATION — SOURCE LATEX
g_j^{\rm num}=\frac{\mathcal L(\theta+\varepsilon e_j)-\mathcal L(\theta-\varepsilon e_j)}{2\varepsilon}\\r=\frac{\|g^{\rm num}-g\|_2}{\|g^{\rm num}\|_2+\|g\|_2+10^{-12}}

LECTURE À VOIX HAUTE
« Le gradient numérique de coordonnée j vaut la perte en thêta plus epsilon e j, moins la perte en thêta moins epsilon e j, le tout divisé par deux epsilon. »
« r est la norme de la différence des gradients, divisée par la somme de leurs normes et de dix puissance moins douze. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `g_j^{\rm num}` | « g indice j, exposant num » | Approximation numérique de la j-ième composante du gradient. Num est une étiquette, pas une puissance. |
| `\theta` | « thêta » | Vecteur des paramètres au point testé. |
| `\varepsilon` | « epsilon » | Petit pas utilisé pour perturber un paramètre. |
| `e_j` | « e indice j » | Vecteur de base : un à la position j et zéro ailleurs. |
| `\mathcal L(\theta\pm\varepsilon e_j)` | « perte en thêta plus ou moins epsilon e j » | Deux évaluations de la perte, de part et d’autre du point courant. |
| `2\varepsilon` | « deux epsilon » | Distance entre les deux points de calcul. |
| `g^{\rm num},\ g` | « g numérique, g » | Gradient approché et gradient analytique à comparer. |
| `\\|\cdot\\|_2` | « norme deux » | Longueur euclidienne du vecteur. |
| `r` | « erre » | Écart relatif normalisé entre les deux gradients. |
| `10^{-12}` | « dix puissance moins douze » | Petit terme qui évite un dénominateur exactement nul. |

INTERPRÉTATION
La différence centrale estime une dérivée en observant la variation de la perte autour du point courant.

POINT D’ATTENTION
Le petit pas epsilon n’est pas une variable à apprendre. Trop petit, il amplifie l’erreur d’arrondi. Les tirages aléatoires doivent rester identiques entre les deux évaluations.

QUESTION À POSER
Pourquoi la différence finie est-elle coûteuse pour un grand réseau ?

RÉPONSE ATTENDUE
Son coût croît avec le nombre de paramètres vérifiés.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 37. AUTOGRAD : CE QUI EST AUTOMATISÉ

DIAPOSITIVE 37 — AUTOGRAD : CE QUI EST AUTOMATISÉ

EXPLICATION TECHNIQUE
Autograd applique un calcul de produits vecteur-Jacobienne en mode inverse, sans former toutes les Jacobiennes denses. Les activations nécessaires au passage arrière sont conservées, ce qui explique une partie de la mémoire d'entraînement. requires_grad indique quels tenseurs participent au calcul différentiel. detach coupe une relation dans le graphe, tandis qu'un contexte no_grad ou inference_mode évite d'enregistrer des opérations destinées à l'évaluation. Préciser que model.eval() change le comportement de certaines couches mais ne désactive pas, à lui seul, la construction du graphe. Les gradients s'accumulent tant qu'ils ne sont pas remis à zéro.

QUESTION À POSER
model.eval() désactive-t-il les gradients ?

RÉPONSE ATTENDUE
Non : utiliser aussi no_grad ou inference_mode pour l’évaluation.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 38. BOUCLE D’ENTRAÎNEMENT : INVARIANTS

DIAPOSITIVE 38 — BOUCLE D’ENTRAÎNEMENT : INVARIANTS

EXPLICATION TECHNIQUE
Faire verbaliser la distinction entre époque, batch et étape d'optimisation. Mélanger l'ordre du train d'une époque à l'autre est usuel ; conserver une évaluation déterministe facilite les comparaisons. La perte de l'époque doit être pondérée par le nombre d'exemples lorsque le dernier batch est incomplet, afin de ne pas lui attribuer un poids excessif. Vérifier les types : logits flottants et cibles entières pour une classification multiclasses. Avant une expérience longue, essayer de surapprendre quelques exemples, puis vérifier que le passage en mode évaluation ne modifie aucun poids.

QUESTION À POSER
Pourquoi pondérer les pertes de batches par leurs tailles ?

RÉPONSE ATTENDUE
Pour retrouver la vraie moyenne par exemple, même avec un dernier batch plus petit.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 39. TP 01 · UN MLP EN NUMPY

DIAPOSITIVE 39 — TP 01 · UN MLP EN NUMPY

EXPLICATION TECHNIQUE
Organisation : 20 minutes pour lire les données et les formes, 40 minutes pour annoter le calcul du gradient, 25 minutes pour le contrôle numérique, 40 minutes d'expériences et 25 minutes de restitution. Le notebook étudiant contient une base exécutable et des consignes d'investigation. Faire prédire l'effet d'un grand taux d'apprentissage avant de l'essayer. Les prétraitements sont ajustés sur le train. Les réponses doivent distinguer erreur d'implémentation, difficulté d'optimisation et manque de généralisation. Les corrigés proposent des conclusions attendues sans imposer un score unique.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Une configuration, une graine, des courbes, un contrôle du gradient et une limite identifiée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 40. DIAGNOSTIQUER AVANT D’AJOUTER DES COUCHES

Symptôme | Vérification prioritaire
Perte constante | Gradients, taux d’apprentissage, paramètres entraînables
NaN ou inf | Logits, normalisation, division et pas trop grand
Train bon, validation faible | Split, surapprentissage, décalage de distribution
Score presque parfait dès le début | Fuite de cible ou duplication train/test
Gradients NumPy ≠ numériques | Axes, transpose, facteur de moyenne et ReLU

DIAPOSITIVE 40 — DIAGNOSTIQUER AVANT D’AJOUTER DES COUCHES

EXPLICATION TECHNIQUE
Cette liste doit être appliquée dans l'ordre. Une erreur de forme, de cible ou de réduction peut produire une courbe qui ressemble à un mauvais choix d'hyperparamètre. Examiner ensuite les normes de gradients et la capacité à ajuster un très petit sous-ensemble. Si le train progresse mais pas la validation, l'optimisation fonctionne probablement : investiguer la régularisation, le protocole et les données. Une fuite de cible peut au contraire donner des résultats artificiellement excellents. Demander à chaque binôme d'associer un symptôme à une vérification falsifiable, plutôt qu'à une solution automatique.

QUESTION À POSER
Quelle première expérience distingue souvent un bug d’un problème de généralisation ?

RÉPONSE ATTENDUE
Essayer de surapprendre un très petit lot d’exemples.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 41. EXERCICE · RECONSTRUIRE LE GRADIENT

DIAPOSITIVE 41 — EXERCICE · RECONSTRUIRE LE GRADIENT

EXPLICATION TECHNIQUE
Accorder dix minutes de travail individuel puis mettre les propositions en commun. Pour un exemple colonne, W1 est 4×3, b1 est 4, a1 est 4, W2 est 2×4, b2 est 2. Le total est 12+4+8+2=26. La sortie a deux logits et delta2=p-y. Le gradient W2 est delta2 a1 transposée ; delta1=(W2 transposée delta2) multiplié élément par élément par l'indicatrice z1>0. Le gradient W1 est delta1 x transposée. Pour un batch, les activations passent en lignes et les produits changent d'ordre, sans changer le modèle.

QUESTION À POSER
Quel est le nombre total de paramètres ?

RÉPONSE ATTENDUE
26 : 16 dans la première couche et 10 dans la seconde.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 42. JOUR 1 · À RETENIR

DIAPOSITIVE 42 — JOUR 1 · À RETENIR

EXPLICATION TECHNIQUE
Clore la séance par une explication sans code : demander à un étudiant de décrire le trajet d'un exemple jusqu'à la perte, puis le trajet d'un gradient jusqu'à un poids de la première couche. Faire nommer le rôle du batch et de la moyenne. L'autre vérification consiste à faire calculer un gradient de biais et à expliquer pourquoi il est une somme dans la version vectorisée. Annoncer la journée suivante : une fois les gradients corrects, il reste à rendre l'optimisation stable et à utiliser une structure adaptée aux images.

QUESTION À POSER
Quelle opération est commune à tous les réseaux différentiables étudiés ?

RÉPONSE ATTENDUE
Composer des transformations et propager les sensibilités par la règle de la chaîne.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 43. OPTIMISATION ET CONVOLUTIONS

DIAPOSITIVE 43 — OPTIMISATION ET CONVOLUTIONS

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 44. JOUR 2 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Optimisation | Mini-batches, Adam, initialisation et régularisation | 90
CNN | Convolution, formes, paramètres et pooling | 105
Exercices | Calcul à la main et champ réceptif | 45
TP 02 | Petit CNN sur digits et expériences contrôlées | 150
Synthèse | Diagnostic et restitution | 30

DIAPOSITIVE 44 — JOUR 2 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 45. SGD ET MINI-BATCHES

DIAPOSITIVE 45 — SGD ET MINI-BATCHES

EXPLICATION TECHNIQUE
Le gradient de mini-batch est un estimateur du gradient empirique lorsque l'échantillonnage est approprié. Sa variabilité influence la trajectoire de l'optimisation, sans constituer une garantie de meilleure généralisation. Doubler le batch réduit le nombre d'étapes par époque ; comparer seulement le nombre d'époques peut donc masquer un changement de budget de mises à jour. La mémoire des activations croît avec B, alors que celle des paramètres reste fixe. Les relations simples de redimensionnement du taux d'apprentissage sont des heuristiques qui nécessitent une validation.

ÉQUATION — SOURCE LATEX
g_t=\frac1B\sum_{i\in\mathcal B_t}\nabla_\theta\ell_i(\theta_t),\qquad\theta_{t+1}=\theta_t-\eta_tg_t

LECTURE À VOIX HAUTE
« g t vaut un sur B fois la somme des gradients des pertes des exemples dont l’indice appartient au mini-batch à l’itération t. »
« Thêta t plus un vaut thêta t moins êta t fois g t. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `g_t` | « gé indice t » | Gradient moyen du mini-batch courant. |
| `B` | « bé » | Nombre d’exemples du mini-batch. |
| `\mathcal B_t` | « bé calligraphique indice t » | Ensemble des indices des exemples choisis à l’itération t. |
| `i\in\mathcal B_t` | « i appartient au mini-batch bé t » | La somme porte seulement sur ces exemples. |
| `\ell_i(\theta_t)` | « ell indice i évaluée en thêta t » | Perte de l’exemple i avec les paramètres courants. |
| `\nabla_\theta` | « gradient par rapport à thêta » | Dérivées selon les paramètres du modèle. |
| `\eta_t` | « êta indice t » | Taux d’apprentissage de cette mise à jour. |
| `\theta_t,\ \theta_{t+1}` | « thêta t, thêta t plus un » | Paramètres courants et paramètres mis à jour. |

INTERPRÉTATION
SGD remplace le gradient de tout l’échantillon par une estimation calculée sur un sous-ensemble.

POINT D’ATTENTION
B est une taille, alors que B calligraphique t est un ensemble d’indices. L’échelle du gradient dépend du choix somme ou moyenne.

QUESTION À POSER
Si N=1000 et B=128 sans drop_last, combien d’étapes par époque ?

RÉPONSE ATTENDUE
8, dont une dernière étape de 104 exemples.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 46. MOMENTUM : MÉMORISER UNE DIRECTION

DIAPOSITIVE 46 — MOMENTUM : MÉMORISER UNE DIRECTION

EXPLICATION TECHNIQUE
Présenter explicitement la convention employée : ici, on n'introduit pas le facteur 1-beta devant g. Une autre écriture utilise une moyenne exponentielle normalisée et nécessite un taux effectif différent. Lorsque les gradients gardent un même signe, leur contribution s'accumule et accélère le mouvement ; lorsqu'ils oscillent, une partie se compense. Une mémoire importante peut aussi provoquer un dépassement ou retarder un changement de direction. Le momentum n'élimine donc pas le choix du taux d'apprentissage. Initialiser v à zéro et calculer deux étapes pour un gradient constant.

ÉQUATION — SOURCE LATEX
v_t=\beta v_{t-1}+g_t,\qquad\theta_{t+1}=\theta_t-\eta v_t

LECTURE À VOIX HAUTE
« v t vaut bêta fois v t moins un, plus g t. »
« Thêta t plus un vaut thêta t moins êta fois v t. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `v_t` | « vé indice t » | Accumulateur de gradients, ou vitesse, au pas courant. |
| `v_{t-1}` | « vé indice t moins un » | État de l’accumulateur au pas précédent. |
| `\beta` | « bêta » | Coefficient de mémoire, généralement entre zéro inclus et un exclu. |
| `g_t` | « gé indice t » | Gradient courant. |
| `\eta` | « êta » | Taux d’apprentissage. |
| `\theta_t,\ \theta_{t+1}` | « thêta t, thêta t plus un » | Paramètres avant et après la mise à jour. |
| `t-1` | « té moins un » | Itération précédente, et non soustraction de un à la valeur de v. |

INTERPRÉTATION
La direction du pas tient compte de plusieurs gradients successifs.

POINT D’ATTENTION
Cette convention du momentum n’ajoute pas de facteur un moins bêta devant g. D’autres conventions normalisent l’accumulateur différemment.

QUESTION À POSER
Avec β=0,9, v0=0 et g=1, quelles sont v1 et v2 ?

RÉPONSE ATTENDUE
1 puis 1,9 dans cette convention.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 47. ADAM : PREMIER ET SECOND MOMENTS

DIAPOSITIVE 47 — ADAM : PREMIER ET SECOND MOMENTS

EXPLICATION TECHNIQUE
Le second moment est une moyenne des carrés, pas directement une estimation de variance centrée. La normalisation produit des échelles de pas différentes selon les coordonnées. Expliquer les facteurs de correction en développant l'espérance de m_t pour un gradient stationnaire : son initialisation à zéro réduit sa magnitude au début. Adam n'exonère pas du réglage du taux ni du contrôle des gradients. Les choix usuels des coefficients sont des points de départ et non des constantes mathématiques. Distinguer la stabilisation numérique epsilon d'une pénalisation du modèle.

ÉQUATION — SOURCE LATEX
\begin{aligned}m_t&=\beta_1m_{t-1}+(1-\beta_1)g_t\\v_t&=\beta_2v_{t-1}+(1-\beta_2)g_t^2\\\theta_{t+1}&=\theta_t-\eta\frac{m_t/(1-\beta_1^t)}{\sqrt{v_t/(1-\beta_2^t)}+\varepsilon}\end{aligned}

LECTURE À VOIX HAUTE
« m t vaut bêta un fois m t moins un, plus un moins bêta un fois le gradient g t. »
« v t vaut bêta deux fois v t moins un, plus un moins bêta deux fois g t au carré, composante par composante. »
« Thêta t plus un vaut thêta t moins êta fois le premier moment corrigé, divisé composante par composante par la racine du second moment corrigé plus epsilon. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `g_t` | « gé indice t » | Gradient au pas t. |
| `m_t,\ m_{t-1}` | « m t, m t moins un » | Moyenne mobile des gradients, courante et précédente. |
| `v_t,\ v_{t-1}` | « vé t, vé t moins un » | Moyenne mobile des carrés des gradients. |
| `\beta_1,\ \beta_2` | « bêta un, bêta deux » | Coefficients de mémoire des deux moyennes. |
| `g_t^2` | « gé t au carré, terme à terme » | Chaque composante du gradient est élevée au carré. |
| `\beta_1^t,\ \beta_2^t` | « bêta un puissance t, bêta deux puissance t » | Puissances utilisées pour corriger l’initialisation à zéro des moments. |
| `m_t/(1-\beta_1^t)` | « m t divisé par un moins bêta un puissance t » | Premier moment corrigé. |
| `v_t/(1-\beta_2^t)` | « vé t divisé par un moins bêta deux puissance t » | Second moment corrigé. |
| `\sqrt{\cdot}` | « racine carrée » | Racine prise composante par composante. |
| `\eta,\ \varepsilon` | « êta, epsilon » | Taux d’apprentissage et petit stabilisateur numérique du dénominateur. |
| `\theta_t,\ \theta_{t+1}` | « thêta t, thêta t plus un » | Paramètres avant et après la mise à jour. |

INTERPRÉTATION
Adam mémorise la direction moyenne du gradient et adapte l’échelle du pas à chaque paramètre.

POINT D’ATTENTION
v est un second moment non centré, pas une variance centrée. Les divisions sont terme à terme. Epsilon se trouve hors de la racine dans la convention affichée.

QUESTION À POSER
Le v d’Adam est-il exactement la variance du gradient ?

RÉPONSE ATTENDUE
Non : c’est un second moment non centré.

LECTURES ET RÉFÉRENCES
Kingma et Ba — Adam, 2014
https://arxiv.org/abs/1412.6980

## 48. INITIALISATION ET PROPAGATION DES VARIANCES

DIAPOSITIVE 48 — INITIALISATION ET PROPAGATION DES VARIANCES

EXPLICATION TECHNIQUE
L'argument de variance suppose approximativement des composantes indépendantes et centrées. Une somme de d contributions indépendantes additionne leurs variances ; il faut donc compenser l'augmentation de fan-in. ReLU élimine une partie du signal, d'où le facteur deux dans l'heuristique de He. Ces conditions idéalisées ne prouvent pas la stabilité de tout réseau réel, mais fournissent un point de départ utile. Les biais peuvent être initialisés à zéro sans rendre tous les neurones identiques si les poids sont aléatoires. Ne pas dire que tous les paramètres doivent nécessairement être aléatoires.

ÉQUATION — SOURCE LATEX
W_{ij}\sim\mathcal N\!\left(0,\frac{2}{d_{\rm in}}\right)\quad\text{(ReLU)},\qquad\operatorname{Var}(W_{ij})\approx\frac{2}{d_{\rm in}+d_{\rm out}}\quad\text{(Xavier)}

LECTURE À VOIX HAUTE
« W i j suit une loi normale de moyenne zéro et de variance deux sur d entrée, pour l’initialisation adaptée à ReLU. »
« Pour Xavier, la variance de W i j vaut approximativement deux divisé par d entrée plus d sortie. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `W_{ij}` | « w indices i j » | Poids reliant une composante d’entrée à une unité de sortie. |
| `\sim` | « suit la loi » | Le poids est tiré aléatoirement selon la distribution indiquée. |
| `\mathcal N(0,v)` | « loi normale de moyenne zéro et de variance vé » | Dans cette convention, le deuxième argument est la variance. |
| `d_{\rm in},\ d_{\rm out}` | « d entrée, d sortie » | Nombre de connexions d’entrée et nombre d’unités de sortie de la couche. |
| `\operatorname{Var}(W_{ij})` | « variance de w i j » | Dispersion des tirages de ce poids autour de leur moyenne. |
| `2/d_{\rm in}` | « deux sur d entrée » | Variance de l’initialisation indiquée pour ReLU. |
| `2/(d_{\rm in}+d_{\rm out})` | « deux sur la somme de d entrée et d sortie » | Variance utilisée dans l’heuristique de Xavier. |
| `\approx` | « environ égal à » | Expression inscrite dans une analyse simplifiée des variances. |

INTERPRÉTATION
L’échelle des poids compense le nombre de contributions additionnées par chaque neurone.

POINT D’ATTENTION
La variance deux sur d entrée n’est pas l’écart-type. L’écart-type correspondant est sa racine carrée.

QUESTION À POSER
Pourquoi ne pas initialiser tous les poids d’une couche à la même valeur ?

RÉPONSE ATTENDUE
Les neurones peuvent rester symétriques et apprendre des représentations identiques.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 49. GRADIENTS QUI DISPARAISSENT OU EXPLOSENT

DIAPOSITIVE 49 — GRADIENTS QUI DISPARAISSENT OU EXPLOSENT

EXPLICATION TECHNIQUE
Une succession d'opérateurs contractants peut atténuer le signal, tandis que des directions amplifiées peuvent le faire exploser. Les normes spectrales donnent une intuition, mais la direction effective du gradient et les corrélations entre matrices comptent aussi. Le clipping par norme limite la magnitude d'un gradient déjà calculé ; il ne restaure pas un gradient disparu et ne corrige pas un masque erroné. Observer les normes par couche avant de proposer une intervention. Les connexions résiduelles introduisent un chemin identité, que nous retrouverons dans ResNet et dans les Transformers.

ÉQUATION — SOURCE LATEX
\frac{\partial\ell}{\partial a_0}=J_1^\top J_2^\top\cdots J_L^\top\frac{\partial\ell}{\partial a_L}

LECTURE À VOIX HAUTE
« Le gradient de la perte selon a zéro vaut J un transposée, fois J deux transposée, et ainsi de suite jusqu’à J grand L transposée, appliquées au gradient de la perte selon a grand L. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `a_0,\ a_L` | « a zéro, a grand ell » | Activations d’entrée et de sortie de la pile. |
| `L` | « grand ell » | Nombre de couches ou de transformations. |
| `J_\ell` | « ji indice ell » | Jacobienne de a ell par rapport à a ell moins un : matrice des dérivées locales. |
| `J_\ell^\top` | « ji indice ell transposée » | Opérateur qui propage un gradient colonne vers la couche précédente. |
| `\frac{\partial\ell}{\partial a_0}` | « gradient de ell par rapport à a zéro » | Sensibilité de la perte aux activations d’entrée. |
| `\frac{\partial\ell}{\partial a_L}` | « gradient de ell par rapport à a grand ell » | Gradient disponible au sommet de la pile. |
| `\cdots` | « et ainsi de suite » | Produits des jacobiennes des couches intermédiaires. |

INTERPRÉTATION
La rétropropagation applique successivement les transformations locales au gradient de sortie.

POINT D’ATTENTION
Dans le produit écrit, J grand L transposée agit d’abord sur le vecteur à droite. Une accumulation de contractions ou d’amplifications peut modifier fortement la norme du gradient.

QUESTION À POSER
Le clipping permet-il de récupérer des gradients proches de zéro ?

RÉPONSE ATTENDUE
Non : il borne les grands gradients, il ne recrée pas les petits.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 50. PÉNALISATION L2 ET WEIGHT DECAY

DIAPOSITIVE 50 — PÉNALISATION L2 ET WEIGHT DECAY

EXPLICATION TECHNIQUE
Pour SGD sans adaptation, développer la mise à jour donne (1-eta lambda) theta moins eta fois le gradient de données. Avec Adam, introduire lambda theta dans le gradient modifie aussi les estimations des moments ; ce n'est donc pas en général la même opération qu'une décroissance séparée du paramètre. AdamW effectue ce découplage. En pratique, certains groupes de paramètres, tels que les biais ou les gains de normalisation, peuvent recevoir des réglages différents. Ce choix doit être documenté dans une comparaison. La pénalisation peut aider mais ne remplace pas un protocole de validation valide.

ÉQUATION — SOURCE LATEX
\mathcal L_{\rm reg}=\mathcal L+\frac\lambda2\|\theta\|_2^2,\qquad\nabla\mathcal L_{\rm reg}=\nabla\mathcal L+\lambda\theta

LECTURE À VOIX HAUTE
« La perte régularisée vaut la perte de données plus lambda sur deux fois la norme deux de thêta au carré. »
« Son gradient vaut le gradient de la perte de données plus lambda fois thêta. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\mathcal L,\ \mathcal L_{\rm reg}` | « grand ell, grand ell indice reg » | Perte de données et perte avec pénalisation. |
| `\theta` | « thêta » | Vecteur des paramètres auxquels on applique la pénalisation. |
| `\lambda` | « lambda » | Coefficient non négatif qui règle la force de la pénalisation. |
| `\\|\theta\\|_2` | « norme deux de thêta » | Longueur euclidienne du vecteur des paramètres. |
| `\\|\theta\\|_2^2` | « norme deux de thêta au carré » | Somme des carrés des paramètres. |
| `\lambda/2` | « lambda sur deux » | Facteur choisi pour que la dérivée de la pénalisation soit lambda thêta. |
| `\nabla` | « nabla, gradient » | Toutes les dérivées de cette ligne sont prises par rapport à theta. |
| `\lambda\theta` | « lambda fois thêta » | Contribution de la pénalisation au gradient. |

INTERPRÉTATION
La pénalisation ajoute un coût lorsque les coefficients deviennent grands.

POINT D’ATTENTION
Le gradient de la perte et celui de la pénalisation s’additionnent. Dans Adam, pénalisation L2 et weight decay découplé ne sont pas généralement équivalents.

QUESTION À POSER
L2 et weight decay sont-ils interchangeables dans toutes les méthodes ?

RÉPONSE ATTENDUE
Non, notamment avec les optimiseurs adaptatifs.

LECTURES ET RÉFÉRENCES
Loshchilov et Hutter — Decoupled Weight Decay Regularization, 2017
https://arxiv.org/abs/1711.05101

## 51. DROPOUT : TRAIN ET ÉVALUATION

DIAPOSITIVE 51 — DROPOUT : TRAIN ET ÉVALUATION

EXPLICATION TECHNIQUE
La formule utilise p comme probabilité de suppression. Vérifier cette convention, car certaines présentations utilisent au contraire une probabilité de conservation. La conservation de l'espérance d'une activation ne signifie pas que l'espérance de toute la sortie du réseau est inchangée : les couches suivantes sont non linéaires. Un taux trop fort peut empêcher l'ajustement du train. Pour une vérification numérique des gradients, le masque doit rester fixe ou le dropout doit être désactivé. En PyTorch, train() et eval() pilotent ce comportement sans modifier automatiquement requires_grad.

ÉQUATION — SOURCE LATEX
m_j\sim\operatorname{Bernoulli}(1-p),\qquad\tilde a_j=\frac{m_j}{1-p}a_j,\qquad\mathbb E[\tilde a_j]=a_j

LECTURE À VOIX HAUTE
« m j suit une loi de Bernoulli dont la probabilité de conservation est un moins p. »
« a tilde j vaut m j divisé par un moins p, puis multiplié par a j. »
« L’espérance de a tilde j vaut a j. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `a_j` | « a indice j » | Activation avant dropout. |
| `m_j` | « m indice j » | Masque aléatoire égal à zéro ou à un. |
| `p,\ 1-p` | « pé, un moins pé » | Probabilité de suppression et probabilité de conservation. On suppose zéro inférieur ou égal à p et p strictement inférieur à un. |
| `\sim\operatorname{Bernoulli}(1-p)` | « suit une loi de Bernoulli de paramètre un moins p » | Le masque vaut un avec probabilité un moins p. |
| `\tilde a_j` | « a tilde indice j » | Activation après application du masque et remise à l’échelle. |
| `\frac{m_j}{1-p}a_j` | « m j sur un moins p, fois a j » | Activation annulée ou amplifiée pour préserver son espérance. |
| `\mathbb E[\tilde a_j]` | « espérance de a tilde j » | Moyenne théorique sur les tirages du masque, pour a j fixé. |

INTERPRÉTATION
Le dropout inversé conserve en moyenne chaque activation grâce à la division par la probabilité de conservation.

POINT D’ATTENTION
Le tilde marque ici une activation modifiée, pas une estimation de probabilité. Préserver l’espérance de cette activation ne préserve pas forcément celle de toute la sortie du réseau.

QUESTION À POSER
Pourquoi diviser par 1-p pendant le train ?

RÉPONSE ATTENDUE
Pour conserver l’espérance de l’activation dans le dropout inversé.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 52. NORMALISER LES ACTIVATIONS

DIAPOSITIVE 52 — NORMALISER LES ACTIVATIONS

EXPLICATION TECHNIQUE
Le point essentiel est de demander sur quels axes sont calculés moyenne et variance. BatchNorm utilise des statistiques regroupant plusieurs exemples et éventuellement des positions spatiales ; LayerNorm travaille à l'intérieur d'un exemple ou d'un token sur ses caractéristiques. Gamma et beta sont appris par gradient et ont des formes dépendant de la normalisation. Epsilon rend la division définie et influence le comportement lorsque la variance est très faible. Il faut distinguer ces normalisations internes du prétraitement global des entrées et des statistiques mobiles utilisées par BatchNorm à l'évaluation.

ÉQUATION — SOURCE LATEX
\hat x=\frac{x-\mu}{\sqrt{\sigma^2+\varepsilon}},\qquad y=\gamma\hat x+\beta

LECTURE À VOIX HAUTE
« x chapeau vaut x moins mu, le tout divisé par la racine carrée de sigma au carré plus epsilon. »
« y vaut gamma fois x chapeau plus bêta. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `x,\ \hat x` | « x, x chapeau » | Activation initiale puis activation normalisée. |
| `\mu` | « mu » | Moyenne calculée sur les axes retenus par la normalisation. |
| `\sigma^2` | « sigma au carré » | Variance sur ces mêmes axes. |
| `\varepsilon` | « epsilon » | Petit nombre positif qui stabilise le dénominateur. |
| `\sqrt{\sigma^2+\varepsilon}` | « racine carrée de sigma au carré plus epsilon » | Échelle de normalisation. |
| `\gamma,\ \beta` | « gamma, bêta » | Gain multiplicatif et décalage appris. |
| `y` | « y » | Activation de sortie après transformation affine. |
| `\hat x` | « chapeau » | Indique ici une normalisation, alors que y chapeau désigne une prédiction dans la perte de régression. |

INTERPRÉTATION
On centre l’activation, on ajuste son échelle, puis on lui applique un gain et un décalage appris.

POINT D’ATTENTION
Les axes des statistiques dépendent de la méthode : BatchNorm et LayerNorm ne calculent pas les mêmes moyennes. Sigma au carré est une variance, pas l’activation sigmoïde.

QUESTION À POSER
Peut-on comparer BatchNorm et LayerNorm sans préciser les axes ?

RÉPONSE ATTENDUE
Non : les axes définissent l’opération.

LECTURES ET RÉFÉRENCES
Ioffe et Szegedy — Batch Normalization, 2015
https://arxiv.org/abs/1502.03167

Ba et al. — Layer Normalization, 2016
https://arxiv.org/abs/1607.06450

## 53. EARLY STOPPING ET COURBES D’APPRENTISSAGE

DIAPOSITIVE 53 — EARLY STOPPING ET COURBES D’APPRENTISSAGE

EXPLICATION TECHNIQUE
Les courbes de cette diapositive sont illustratives et non les résultats d'un benchmark. Elles montrent un cas où la perte train continue de diminuer alors que la validation remonte. La règle d'arrêt doit préciser le critère, la direction d'amélioration, la patience et le changement minimal considéré. Sauvegarder réellement le meilleur état des poids, pas seulement l'indice de la meilleure époque. Tester plusieurs règles sur le même test revient à l'utiliser pour la sélection. Une seule séparation ne mesure pas toute la variabilité ; répéter sur plusieurs graines peut être utile si le budget le permet.

QUESTION À POSER
Pourquoi restaurer le meilleur checkpoint ?

RÉPONSE ATTENDUE
La dernière époque n’est pas nécessairement celle qui généralise le mieux.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 54. POURQUOI UN CNN POUR UNE IMAGE ?

DIAPOSITIVE 54 — POURQUOI UN CNN POUR UNE IMAGE ?

EXPLICATION TECHNIQUE
Comparer une image à un vecteur aplati. Une couche dense peut en principe apprendre des relations entre pixels, mais elle ne reçoit pas explicitement l'hypothèse qu'un motif local est réutilisable dans l'espace. La convolution introduit cette hypothèse dans la paramétrisation. Le partage réduit le nombre de paramètres et crée une équivariance sous certaines conditions. Il ne garantit pas l'invariance aux translations du modèle complet. Les effets de bord, le stride, le pooling et les couches finales peuvent modifier cette propriété. L'utilité du biais inductif dépend de la tâche et des transformations pertinentes.

QUESTION À POSER
Pourquoi le même noyau est-il appliqué à plusieurs positions ?

RÉPONSE ATTENDUE
Pour partager un détecteur local et ses paramètres dans l’espace.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

## 55. CONVOLUTION 2D : L’OPÉRATION LOCALE

DIAPOSITIVE 55 — CONVOLUTION 2D : L’OPÉRATION LOCALE

EXPLICATION TECHNIQUE
La formule correspond au cas stride un, sans dilation et sans padding, avec un batch omis pour la lisibilité. Une convolution mathématique retourne le noyau ; l'opération usuelle des couches Conv2d est une corrélation croisée. Puisque les coefficients sont appris, cette convention ne réduit pas la famille de détecteurs représentable. Chaque canal de sortie possède un ensemble de noyaux sur tous les canaux d'entrée et un biais. Un filtre RGB a donc trois plans de coefficients, pas un seul noyau recopié mécaniquement sur rouge, vert et bleu.

ÉQUATION — SOURCE LATEX
Y_{o,i,j}=b_o+\sum_{c=1}^{C_{\rm in}}\sum_{u=0}^{k_h-1}\sum_{v=0}^{k_w-1}W_{o,c,u,v}\,X_{c,i+u,j+v}

LECTURE À VOIX HAUTE
« Y aux indices o, i, j vaut le biais du canal o plus une somme sur les canaux c, les décalages verticaux u et horizontaux v, des poids W o c u v multipliés par les entrées X c, i plus u, j plus v. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X,\ Y` | « grand x, grand y » | Tenseur d’entrée et tenseur de sortie. L’axe batch est omis ici. |
| `o,\ c` | « o, cé » | Indice du canal de sortie et indice du canal d’entrée. |
| `i,\ j` | « i, j » | Position spatiale de la sortie. |
| `u,\ v` | « u, vé » | Décalages à l’intérieur du noyau. |
| `C_{\rm in}` | « cé entrée » | Nombre de canaux d’entrée. |
| `k_h,\ k_w` | « k hauteur, k largeur » | Hauteur et largeur du noyau. |
| `W_{o,c,u,v}` | « w indices o, c, u, v » | Coefficient du noyau reliant le canal c au canal o au décalage u, v. |
| `X_{c,i+u,j+v}` | « x au canal c, ligne i plus u, colonne j plus v » | Valeur d’entrée couverte par ce coefficient. |
| `b_o` | « bé indice o » | Biais commun à toutes les positions du canal de sortie o. |
| `\sum_c\sum_u\sum_v` | « somme sur c, puis sur u, puis sur v » | Addition de toutes les contributions des canaux et de la fenêtre. |

INTERPRÉTATION
Une valeur de sortie combine une fenêtre locale de tous les canaux d’entrée avec les coefficients d’un filtre.

POINT D’ATTENTION
C’est la corrélation croisée utilisée par Conv2d, avec stride un, dilation un et sans padding dans cet exemple. Les indices u et v commencent à zéro.

QUESTION À POSER
Un filtre 3×3 sur une entrée RGB contient-il 9 poids ?

RÉPONSE ATTENDUE
Non : il contient 3×3×3 = 27 poids, plus un biais éventuel.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

## 56. CONVOLUTION : EXEMPLE À LA MAIN

DIAPOSITIVE 56 — CONVOLUTION : EXEMPLE À LA MAIN

EXPLICATION TECHNIQUE
Faire remplir les quatre cases avant d'afficher le calcul oralement. La première vaut 1×1+2×0+0×0+1×(-1)=0. La deuxième vaut 2-3=-1, la troisième 0-1=-1 et la quatrième 1-0=1. Insister sur le fait qu'un seul jeu de quatre poids a produit toutes les sorties. Un biais s'ajouterait à chaque case du même canal. Ce noyau est fixé à titre pédagogique ; dans un CNN, il est généralement appris. Le calcul est une corrélation croisée valide et ne doit pas être mélangé à une convention de noyau retourné.

ÉQUATION — SOURCE LATEX
X=\begin{bmatrix}1&2&0\\0&1&3\\2&1&0\end{bmatrix},\quad W=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\\Y=\begin{bmatrix}0&-1\\-1&1\end{bmatrix}

LECTURE À VOIX HAUTE
« X est une matrice trois par trois. Ses lignes sont : un, deux, zéro ; zéro, un, trois ; deux, un, zéro. »
« W est une matrice deux par deux dont les lignes sont un, zéro, puis zéro, moins un. »
« Y est la matrice deux par deux : zéro, moins un, puis moins un, un. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X` | « grand x » | Image d’entrée de hauteur trois et de largeur trois. |
| `W` | « w » | Noyau de hauteur deux et de largeur deux. |
| `Y` | « grand y » | Carte de sortie, obtenue avec un pas de un et sans padding. |
| `\begin{bmatrix}a&b\\c&d\end{bmatrix}` | « matrice deux par deux, première ligne a b, deuxième ligne c d » | Les crochets regroupent des valeurs en lignes et colonnes. |
| `-1` | « moins un » | Poids négatif du coin inférieur droit du noyau, ou valeur négative de sortie selon sa position. |
| `=` | « égale » | Attribue explicitement ses valeurs à chaque matrice. |

INTERPRÉTATION
À chaque position, le noyau soustrait le coin inférieur droit de la fenêtre à son coin supérieur gauche. La première sortie vaut un moins un, donc zéro.

POINT D’ATTENTION
Le noyau n’est pas retourné dans ce calcul. La lecture de la matrice se fait ligne par ligne, sans traiter les crochets comme une norme.

QUESTION À POSER
Combien de paramètres seraient appris avec un biais ?

RÉPONSE ATTENDUE
5 : quatre poids et un biais.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 57. STRIDE, PADDING ET DILATION

DIAPOSITIVE 57 — STRIDE, PADDING ET DILATION

EXPLICATION TECHNIQUE
Définir le noyau effectif : d(k-1)+1. On compte ensuite le nombre de positions valides de cette fenêtre après ajout du padding. La formule présentée utilise un padding symétrique et s'applique indépendamment à la hauteur et à la largeur. Pour H=32, k=3, p=1, d=1 et s=2, la sortie vaut 16. Un padding dit same ne signifie pas la même chose pour tous les strides et toutes les bibliothèques ; dans les versions étudiées, vérifier les contraintes de l'API. La dilation augmente le champ couvert sans augmenter le nombre de coefficients.

ÉQUATION — SOURCE LATEX
H_{\rm out}=\left\lfloor\frac{H+2p-d(k-1)-1}{s}+1\right\rfloor

LECTURE À VOIX HAUTE
« H sortie vaut la partie entière inférieure de la quantité H plus deux p, moins d fois k moins un, moins un, divisée par s, puis plus un. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `H,\ H_{\rm out}` | « ache, ache sortie » | Hauteur de l’entrée et hauteur de la sortie. |
| `p` | « pé » | Nombre de lignes de padding ajoutées de chaque côté. |
| `d` | « dé » | Dilation, c’est-à-dire espacement des coefficients du noyau. |
| `k` | « ka » | Taille du noyau selon cet axe. |
| `s` | « esse » | Stride, ou pas de déplacement de la fenêtre. |
| `d(k-1)+1` | « d fois k moins un, plus un » | Taille effective du noyau après dilation. |
| `\lfloor\cdot\rfloor` | « partie entière inférieure, ou plancher » | Plus grand entier inférieur ou égal à la valeur entre les crochets. |
| `2p` | « deux pé » | Padding total, réparti symétriquement sur les deux bords. |

INTERPRÉTATION
On compte le nombre de positions de la fenêtre qui tiennent dans l’entrée après padding.

POINT D’ATTENTION
Les crochets de plancher demandent d’arrondir vers le bas. Ici d est une dilation, pas une dimension d’embedding. La même formule s’applique indépendamment à la largeur.

QUESTION À POSER
Pour H=28, k=3, p=0, s=1, d=1, quelle hauteur ?

RÉPONSE ATTENDUE
26.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

## 58. CANAUX ET TENSEURS D’UN CNN

Objet | Forme | Rôle
Entrée | B × Cᵢₙ × H × W | Images du batch
Poids | Cₒᵤₜ × Cᵢₙ × kₕ × k𝓌 | Détecteurs partagés
Biais | Cₒᵤₜ | Décalage par canal de sortie
Sortie | B × Cₒᵤₜ × Hₒᵤₜ × Wₒᵤₜ | Cartes de caractéristiques

DIAPOSITIVE 58 — CANAUX ET TENSEURS D’UN CNN

EXPLICATION TECHNIQUE
Conserver le batch au premier axe évite de confondre nombre d'images et nombre de canaux. Dans notre convention PyTorch, l'image est B×C×H×W. Une autre bibliothèque peut utiliser B×H×W×C ; l'algèbre est la même mais les axes à manipuler changent. Une convolution de 3 canaux vers 16 canaux produit 16 cartes d'activation, chacune agrégeant les trois canaux d'entrée. La notion de canal de sortie ne signifie pas que ce canal correspond à une classe ; les classes n'apparaissent que dans la tête finale choisie pour la tâche.

QUESTION À POSER
Une carte de caractéristiques correspond-elle nécessairement à une catégorie ?

RÉPONSE ATTENDUE
Non : c’est une représentation intermédiaire apprise.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 59. TAILLES ET NOMBRE DE PARAMÈTRES

DIAPOSITIVE 59 — TAILLES ET NOMBRE DE PARAMÈTRES

EXPLICATION TECHNIQUE
Pour une entrée RGB et 16 filtres 3×3, le nombre de paramètres est 16(3×9+1)=448. Les MACs comptent ici les multiplications-accumulations d'un exemple et omettent les biais. Une convention FLOPs peut compter deux opérations pour une multiplication-accumulation ; il faut annoncer cette convention. Si H et W doublent, les paramètres restent inchangés mais le calcul et les activations sont approximativement multipliés par quatre. Pour des convolutions groupées, le nombre de connexions par canal change ; la formule de cette diapositive doit alors être adaptée.

ÉQUATION — SOURCE LATEX
P=C_{\rm out}(C_{\rm in}k_hk_w+1)\\\operatorname{MACs}\approx H_{\rm out}W_{\rm out}C_{\rm out}C_{\rm in}k_hk_w

LECTURE À VOIX HAUTE
« Le nombre de paramètres vaut C sortie multiplié par la somme de C entrée fois k hauteur fois k largeur et de un. »
« Le nombre de multiplications-accumulations vaut approximativement H sortie fois W sortie fois C sortie fois C entrée fois k hauteur fois k largeur. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `P` | « pé » | Nombre de paramètres appris, biais inclus. |
| `C_{\rm in},\ C_{\rm out}` | « cé entrée, cé sortie » | Nombre de canaux d’entrée et de sortie. |
| `k_h,\ k_w` | « k hauteur, k largeur » | Dimensions du noyau. |
| `C_{\rm in}k_hk_w` | « cé entrée fois k hauteur fois k largeur » | Nombre de poids utilisés pour une valeur de sortie. |
| `+1` | « plus un » | Un biais supplémentaire par canal de sortie. |
| `H_{\rm out},\ W_{\rm out}` | « ache sortie, w sortie » | Hauteur et largeur de la carte de sortie. |
| `\operatorname{MACs}` | « macs, multiplications-accumulations » | Nombre de produits ajoutés à un accumulateur, pour un exemple. |
| `\approx` | « approximativement égal à » | Le comptage du calcul omet notamment les biais et d’autres opérations. |

INTERPRÉTATION
Les paramètres sont partagés entre les positions, mais le calcul doit être répété à chacune d’elles.

POINT D’ATTENTION
La formule suppose une convolution non groupée. P désigne ici un nombre de paramètres, alors qu’il désigne la taille d’un patch dans la partie ViT.

QUESTION À POSER
Une convolution contient-elle plus de poids lorsqu’on passe de 32×32 à 64×64 ?

RÉPONSE ATTENDUE
Non, à noyau et nombres de canaux constants.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

## 60. POOLING : RÉDUIRE LA RÉSOLUTION

DIAPOSITIVE 60 — POOLING : RÉDUIRE LA RÉSOLUTION

EXPLICATION TECHNIQUE
Expliquer la différence du passage arrière : le max transmet le gradient à une position sélectionnée, tandis que la moyenne le répartit également sur toutes les positions. Les égalités au maximum nécessitent une convention d'implémentation. Le sous-échantillonnage réduit la mémoire et augmente le champ réceptif des couches suivantes, mais détruit de l'information de position. Il ne procure pas une invariance parfaite aux translations. Une convolution à stride supérieur à un peut jouer un rôle de réduction de résolution tout en apprenant sa transformation, avec un autre coût en paramètres.

ÉQUATION — SOURCE LATEX
\operatorname{maxpool}\!\begin{bmatrix}1&4\\2&3\end{bmatrix}=4,\qquad\operatorname{avgpool}\!\begin{bmatrix}1&4\\2&3\end{bmatrix}=2.5

LECTURE À VOIX HAUTE
« Le max-pooling de la fenêtre contenant un, quatre, deux et trois vaut quatre. »
« Le pooling moyen de la même fenêtre vaut deux virgule cinq. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\operatorname{maxpool}` | « max-pooling, ou agrégation par maximum » | Sélection de la plus grande valeur de la fenêtre. |
| `\operatorname{avgpool}` | « average-pooling, ou agrégation par moyenne » | Moyenne arithmétique des valeurs de la fenêtre. |
| `\begin{bmatrix}1&4\\2&3\end{bmatrix}` | « matrice deux par deux : un quatre, puis deux trois » | Fenêtre locale examinée. |
| `4` | « quatre » | Valeur maximale de la fenêtre. |
| `2.5` | « deux virgule cinq » | Moyenne : un plus quatre plus deux plus trois, divisés par quatre. |
| `=` | « égale » | Résultat scalaire de l’agrégation. |

INTERPRÉTATION
Les quatre valeurs de la fenêtre se réduisent à une seule valeur par canal.

POINT D’ATTENTION
Le point de 2.5 est un séparateur décimal dans la formule. Le lire « virgule » en français. Ces opérations de pooling ne possèdent pas de poids appris.

QUESTION À POSER
Où va le gradient d’un max pooling 2×2 sans égalité ?

RÉPONSE ATTENDUE
Vers l’entrée qui a produit le maximum.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 61. CHAMP RÉCEPTIF : CALCUL RÉCURSIF

DIAPOSITIVE 61 — CHAMP RÉCEPTIF : CALCUL RÉCURSIF

EXPLICATION TECHNIQUE
Faire le calcul pour Conv3 stride1, Pool2 stride2, Conv3 stride1. Après la première convolution, r=3 et j=1 ; après le pooling, r=4 et j=2 ; après la seconde convolution, r=8 et j=2. Deux convolutions 3×3 à stride un donnent en revanche un champ de 5×5 avant tout pooling. Le padding déplace les centres et traite les bords, mais n'augmente pas le nombre de pixels réels disponibles en dehors de l'image. Le champ réceptif effectif décrit les influences effectivement importantes, qui dépendent des poids et des données.

ÉQUATION — SOURCE LATEX
j_\ell=j_{\ell-1}s_\ell,\qquad r_\ell=r_{\ell-1}+(k_\ell-1)d_\ell j_{\ell-1}\\r_0=j_0=1

LECTURE À VOIX HAUTE
« Le saut j de la couche ell vaut le saut précédent multiplié par le stride de cette couche. »
« Le champ réceptif r de la couche ell vaut le champ précédent, plus k ell moins un, fois la dilation d ell, fois le saut précédent. »
« Au départ, r zéro et j zéro valent un. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\ell,\ \ell-1` | « ell, ell moins un » | Indices de la couche courante et de la couche précédente. |
| `j_\ell` | « ji indice ell » | Écart entre deux positions voisines de cette couche, mesuré en pixels de l’entrée. |
| `s_\ell` | « esse indice ell » | Stride de la couche. |
| `r_\ell` | « erre indice ell » | Taille du champ réceptif théorique sur un axe. |
| `k_\ell` | « ka indice ell » | Taille du noyau de la couche. |
| `d_\ell` | « dé indice ell » | Dilation de cette couche. |
| `(k_\ell-1)d_\ell j_{\ell-1}` | « k ell moins un, fois d ell, fois j ell moins un » | Étendue supplémentaire couverte dans les coordonnées de l’entrée. |
| `r_0=j_0=1` | « r zéro et j zéro valent un » | Un pixel de l’entrée couvre un pixel et deux pixels voisins sont séparés d’un pas. |

INTERPRÉTATION
Le stride change l’espacement entre les sorties. Les tailles de noyau et les dilations agrandissent le champ couvert.

POINT D’ATTENTION
j est ici un saut spatial, pas un indice de colonne comme dans la convolution. Le champ réceptif théorique ne mesure pas l’influence effective de chaque pixel.

QUESTION À POSER
Quel champ obtient-on avec deux convolutions 3×3 sans stride ?

RÉPONSE ATTENDUE
5×5 dans le cas standard.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 62. ÉQUIVARIANCE ET INVARIANCE

DIAPOSITIVE 62 — ÉQUIVARIANCE ET INVARIANCE

EXPLICATION TECHNIQUE
Sur un domaine infini ou avec des conditions adaptées, une convolution à stride un commute avec une translation entière. Sur une image finie, le padding et les bords limitent cette égalité. Avec un stride supérieur à un, seules certaines translations s'alignent sur la grille de sous-échantillonnage. Un classifieur peut rechercher une certaine invariance via l'agrégation spatiale ou l'augmentation, mais cela n'est pas une conséquence absolue du mot CNN. Pour la segmentation, on souhaite plutôt préserver une relation spatiale entre entrée et sortie ; l'invariance totale serait indésirable.

ÉQUATION — SOURCE LATEX
f(Tx)=T f(x)\quad\text{(equivariance)},\qquad g(Tx)=g(x)\quad\text{(invariance)}

LECTURE À VOIX HAUTE
« f appliquée à T de x est égale à T appliquée à f de x : c’est l’équivariance. »
« g appliquée à T de x est égale à g de x : c’est l’invariance. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `x` | « x » | Entrée du modèle. |
| `T` | « té majuscule » | Transformation de l’entrée, par exemple une translation. |
| `Tx` | « té appliquée à x » | Entrée après transformation. |
| `f,\ g` | « effe, gé » | Fonctions dont on étudie le comportement. |
| `Tf(x)` | « té appliquée à effe de x » | Transformation correspondante de la sortie. |
| `f(Tx)=Tf(x)` | « transformer l’entrée puis calculer, ou calculer puis transformer » | La sortie se transforme de façon cohérente avec l’entrée. |
| `g(Tx)=g(x)` | « la sortie de g reste la même après transformation de l’entrée » | La sortie ne dépend pas de cette transformation. |

INTERPRÉTATION
Équivariance : la sortie suit la transformation. Invariance : la sortie reste identique.

POINT D’ATTENTION
Le même T représente les actions compatibles dans l’espace d’entrée et de sortie. Les bords, le padding et le sous-échantillonnage peuvent limiter ces égalités.

QUESTION À POSER
Une segmentation d’image doit-elle être totalement invariante à la translation ?

RÉPONSE ATTENDUE
Non : le masque devrait généralement se déplacer avec les objets.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 63. TP 02 · CONSTRUIRE UN PETIT CNN

DIAPOSITIVE 63 — TP 02 · CONSTRUIRE UN PETIT CNN

EXPLICATION TECHNIQUE
Déroulé : 20 minutes pour le protocole de séparation, 30 minutes pour les dimensions, 40 minutes pour l'entraînement, 35 minutes pour une ablation et 25 minutes d'analyse. Le réseau de base emploie deux blocs convolution-ReLU-pooling puis une tête dense. Les images sont divisées par 16, échelle définie par le jeu, sans apprentissage sur le test. Les étudiants comparent par exemple le pooling et une réduction par stride, à budget documenté. La petite résolution permet de travailler sur CPU ; les conclusions ne doivent pas être extrapolées directement à des images haute résolution.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Une architecture annotée, un protocole sans fuite et une explication de ses erreurs.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 64. EXERCICE · AUDITER UNE CONVOLUTION

DIAPOSITIVE 64 — EXERCICE · AUDITER UNE CONVOLUTION

EXPLICATION TECHNIQUE
Laisser huit minutes puis faire corriger par un autre binôme. H sortie et W sortie valent chacun floor((32+2-2-1)/2+1)=16. La forme est donc B×16×16×16. Le nombre de paramètres est 16(3×3×3+1)=448. Le coût principal vaut 16×16×16×3×3×3=110592 MACs par image, hors biais et activation. Le batch multiplie ce coût par B sans modifier le nombre de poids. Demander enfin l'effet d'un padding nul : la hauteur devient 15, ce qui modifie le calcul et les activations mais pas les paramètres.

QUESTION À POSER
Combien de MACs, hors biais et activation ?

RÉPONSE ATTENDUE
110 592 par image dans la convention indiquée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 65. JOUR 2 · À RETENIR

DIAPOSITIVE 65 — JOUR 2 · À RETENIR

EXPLICATION TECHNIQUE
Demander une restitution qui relie les deux moitiés de la journée. Les CNN n'ont pas une règle d'apprentissage séparée : ils utilisent la même rétropropagation, avec une structure de partage des poids. Le gradient d'un noyau additionne les contributions de toutes les positions où il a été appliqué et de tous les exemples du batch. Revenir sur le rôle des augmentations et du test pour ne pas confondre une hypothèse d'architecture et une propriété empiriquement validée. La journée suivante introduit le transfert, qui permet de réutiliser des représentations déjà apprises.

QUESTION À POSER
Comment le gradient d’un noyau combine-t-il ses multiples utilisations ?

RÉPONSE ATTENDUE
Il additionne les contributions des positions et des exemples.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 66. CNN ET TRANSFERT

DIAPOSITIVE 66 — CNN ET TRANSFERT

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 67. JOUR 3 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Architectures | CNN complet, BatchNorm et résidus | 60
Données | Augmentation, séparation et métriques | 75
Transfert | Gel, adaptation et expériences comparables | 75
TP 03 | Source digits 0–4 vers cible digits 5–9 | 180
Restitution | Erreurs, résultats et limites | 30

DIAPOSITIVE 67 — JOUR 3 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 68. LE CNN DU TP : PARCOURS D’UN BATCH

Étape | Forme hors batch | Paramètres
Conv 3×3 + ReLU | 8 × 8 × 8 | 80
MaxPool 2×2 | 8 × 4 × 4 | 0
Conv 3×3 + ReLU | 16 × 4 × 4 | 1 168
MaxPool + flatten | 64 | 0
Linear 64 → 10 | 10 logits | 650
Total |  | 1 898

DIAPOSITIVE 68 — LE CNN DU TP : PARCOURS D’UN BATCH

EXPLICATION TECHNIQUE
Ce tableau correspond exactement au réseau des notebooks. Une première convolution 1→8 conserve 8×8 grâce au padding, puis un pooling divise la résolution par deux. Le deuxième bloc 8→16 réduit ensuite 4×4 en 2×2. L'aplatissement donne 16×2×2=64 composantes. Le nombre de paramètres est 80+1168+650=1898 ; ReLU, pooling et flatten n'ajoutent aucun poids. Vérifier ce total avec la somme numel des paramètres PyTorch. L'aplatissement impose ici une taille d'entrée déterminée ; une agrégation globale pourrait rendre la tête moins dépendante de cette taille.

QUESTION À POSER
Pourquoi la tête reçoit-elle 64 entrées ?

RÉPONSE ATTENDUE
16 canaux × 2 × 2 positions.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 69. CONVOLUTION 1×1 ET AGRÉGATION GLOBALE

DIAPOSITIVE 69 — CONVOLUTION 1×1 ET AGRÉGATION GLOBALE

EXPLICATION TECHNIQUE
Un noyau 1×1 n'est pas une opération inutile : il réalise une projection sur les canaux, avec les mêmes poids à chaque position. Il est employé pour réduire ou augmenter la dimension et pour aligner les branches résiduelles. L'agrégation globale par moyenne réduit la dépendance de la tête à la taille spatiale et peut réduire fortement le nombre de paramètres. Elle détruit toutefois la localisation fine ; ce choix convient plus naturellement à certaines tâches de classification qu'à une reconstruction dense. Comparer son coût à celui d'une grande couche dense après aplatissement.

ÉQUATION — SOURCE LATEX
Y_{o,i,j}=b_o+\sum_c W_{o,c}X_{c,i,j},\qquad g_c=\frac1{HW}\sum_{i,j}X_{c,i,j}

LECTURE À VOIX HAUTE
« Y du canal o à la position i j vaut b o plus la somme, sur les canaux c, de W o c fois X c i j. »
« g c vaut un sur H W fois la somme de X c i j sur toutes les positions spatiales. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X_{c,i,j},\ Y_{o,i,j}` | « x canal c position i j ; y canal o position i j » | Activations d’entrée et de sortie à une même position. |
| `c,\ o` | « cé, o » | Canal d’entrée et canal de sortie. |
| `W_{o,c},\ b_o` | « w indices o c, b indice o » | Poids du mélange des canaux et biais du canal de sortie. |
| `\sum_c` | « somme sur cé » | Addition des contributions de tous les canaux d’entrée. |
| `H,\ W` | « ache, w » | Hauteur et largeur de la carte dans la seconde formule. |
| `HW` | « ache fois w » | Nombre total de positions spatiales. |
| `\sum_{i,j}` | « somme sur i et j » | Somme sur toutes les lignes et colonnes. |
| `g_c` | « gé indice cé » | Moyenne spatiale du canal c. |

INTERPRÉTATION
La convolution un par un mélange les canaux à position fixe. La moyenne globale réduit chaque canal à un scalaire.

POINT D’ATTENTION
W avec des indices est un poids, tandis que W seul dans H W désigne la largeur. Les deux opérations décrites ont des rôles distincts.

QUESTION À POSER
Une convolution 1×1 peut-elle modifier le nombre de canaux ?

RÉPONSE ATTENDUE
Oui, via une projection apprise partagée à chaque position.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 70. BATCHNORM DANS UN CNN

DIAPOSITIVE 70 — BATCHNORM DANS UN CNN

EXPLICATION TECHNIQUE
Décrire précisément les axes d'agrégation pour une couche BatchNorm2d. Les paramètres gamma et beta possèdent une composante par canal et ne sont pas les statistiques mobiles. Les premières sont apprises par gradient ; les secondes sont des buffers mis à jour selon le comportement de la couche. Il existe des conventions d'estimation de variance et de mise à jour propres à chaque API ; la formule illustre ici la normalisation du batch. Durant un transfert sur peu de données, adapter ces statistiques peut être nuisible même si les poids convolutionnels sont gelés. D'où l'importance de distinguer gel des paramètres et mode évaluation.

ÉQUATION — SOURCE LATEX
\mu_c=\frac1{BHW}\sum_{b,i,j}X_{b,c,i,j},\quad\hat X_{b,c,i,j}=\frac{X_{b,c,i,j}-\mu_c}{\sqrt{\sigma_c^2+\varepsilon}}

LECTURE À VOIX HAUTE
« Mu c vaut la somme des activations du canal c sur le batch et les positions spatiales, divisée par B fois H fois W. »
« X chapeau aux indices b c i j vaut X b c i j moins mu c, divisé par la racine de sigma c au carré plus epsilon. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `B,\ H,\ W` | « bé, ache, w » | Taille du batch, hauteur et largeur des cartes. |
| `b,\ c,\ i,\ j` | « bé, cé, i, j » | Indices de l’exemple, du canal, de la ligne et de la colonne. |
| `X_{b,c,i,j}` | « x indices b c i j » | Une activation du tenseur d’entrée. |
| `\mu_c` | « mu indice cé » | Moyenne du canal c sur les B H W valeurs du batch. |
| `\sum_{b,i,j}` | « somme sur b, i et j » | Agrégation sur les exemples et les positions, en gardant le canal fixé. |
| `\sigma_c^2` | « sigma indice cé au carré » | Variance calculée sur ces mêmes axes. |
| `\varepsilon` | « epsilon » | Terme positif de stabilisation. |
| `\hat X_{b,c,i,j}` | « x chapeau indices b c i j » | Activation centrée et normalisée. |

INTERPRÉTATION
BatchNorm2d calcule une paire de statistiques pour chaque canal.

POINT D’ATTENTION
b minuscule est ici un indice d’exemple et non un biais. L’écriture montre la normalisation du batch. En évaluation, BatchNorm utilise normalement ses statistiques enregistrées. Le gain gamma et le biais beta peuvent ensuite compléter le calcul.

QUESTION À POSER
requires_grad=False fige-t-il automatiquement les statistiques mobiles ?

RÉPONSE ATTENDUE
Non : elles dépendent aussi du mode train/eval de BatchNorm.

LECTURES ET RÉFÉRENCES
Ioffe et Szegedy — Batch Normalization, 2015
https://arxiv.org/abs/1502.03167

## 71. CONNEXIONS RÉSIDUELLES

DIAPOSITIVE 71 — CONNEXIONS RÉSIDUELLES

EXPLICATION TECHNIQUE
L'écriture résiduelle change la paramétrisation d'un bloc : F peut apprendre une petite correction ou se rapprocher de zéro. Le terme identité offre un chemin direct au signal et au gradient, sans garantir l'absence de toute difficulté d'optimisation. Si le nombre de canaux ou la résolution change, une projection P(x), souvent convolution 1×1 avec stride approprié, remplace l'identité pour rendre l'addition possible. Le gradient du paramètre d'une branche est calculé comme précédemment ; le gradient par rapport à l'entrée additionne les chemins. Cette structure sera centrale dans les blocs Transformers.

ÉQUATION — SOURCE LATEX
y=x+F(x),\qquad\frac{\partial y}{\partial x}=I+\frac{\partial F}{\partial x}

LECTURE À VOIX HAUTE
« y vaut x plus F de x. »
« La jacobienne de y par rapport à x vaut la matrice identité plus la jacobienne de F par rapport à x. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `x,\ y` | « x, y » | Entrée et sortie du bloc, de formes compatibles pour l’addition. |
| `F(x)` | « grand effe de x » | Transformation calculée par la branche résiduelle. |
| `+` | « plus » | Addition des deux branches, composante par composante. |
| `\frac{\partial y}{\partial x}` | « jacobienne de y par rapport à x » | Matrice des dérivées de chaque composante de sortie selon chaque composante d’entrée. |
| `I` | « i majuscule, matrice identité » | Dérivée du chemin direct x. |
| `\frac{\partial F}{\partial x}` | « jacobienne de grand effe par rapport à x » | Dérivée de la branche transformée. |

INTERPRÉTATION
Le chemin direct contribue une identité à la dérivée, en plus du chemin qui traverse la transformation F.

POINT D’ATTENTION
Il s’agit d’une jacobienne lorsque x et y sont vectoriels. Une branche projetée possède la dérivée de sa projection au lieu d’une identité stricte.

QUESTION À POSER
Peut-on ajouter directement B×16×16×16 et B×32×8×8 ?

RÉPONSE ATTENDUE
Non : il faut aligner les dimensions par une projection adaptée.

LECTURES ET RÉFÉRENCES
He et al. — Deep Residual Learning for Image Recognition, 2015
https://arxiv.org/abs/1512.03385

## 72. AUGMENTER SANS CHANGER LA CIBLE

DIAPOSITIVE 72 — AUGMENTER SANS CHANGER LA CIBLE

EXPLICATION TECHNIQUE
Une rotation légère peut être acceptable pour certains chiffres, mais une rotation de 180 degrés peut échanger des significations. Un retournement horizontal peut être adapté à une photographie d'objet et incorrect pour du texte. Pour une segmentation, il faut transformer la cible spatiale de façon cohérente. La formule suppose ici que T conserve la classe ; cette hypothèse doit être vérifiée. Une augmentation ne crée pas un nouvel individu indépendant pour le test : toutes les variantes d'une même observation doivent rester dans la même partition. Documenter la politique et ses probabilités dans le compte rendu.

ÉQUATION — SOURCE LATEX
\mathcal L_{\rm aug}=\mathbb E_{(x,y)}\,\mathbb E_{T\sim\mathcal A}\!\left[\ell(f_\theta(Tx),y)\right]

LECTURE À VOIX HAUTE
« La perte avec augmentation est l’espérance, sur les exemples x y, de l’espérance sur une transformation T tirée selon la politique A, de la perte entre la prédiction sur T x et la cible y. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\mathcal L_{\rm aug}` | « grand ell indice aug » | Perte qui tient compte des transformations aléatoires des entrées. |
| `\mathbb E` | « espérance » | Moyenne théorique selon la distribution indiquée en indice. |
| `(x,y)` | « couple x y » | Observation et cible associée. |
| `T` | « té majuscule » | Transformation aléatoire appliquée à une entrée. |
| `T\sim\mathcal A` | « té tirée selon a calligraphique » | La politique d’augmentation A définit les transformations et leurs probabilités. |
| `Tx` | « té appliquée à x » | Exemple transformé. |
| `f_\theta(Tx)` | « f thêta de té x » | Prédiction du modèle sur cet exemple transformé. |
| `\ell(f_\theta(Tx),y)` | « perte entre la prédiction transformée et y » | Erreur d’apprentissage avec la cible de classe conservée. |

INTERPRÉTATION
L’objectif demande au modèle de fonctionner sur plusieurs transformations admissibles du même exemple.

POINT D’ATTENTION
La formule suppose que T conserve la cible. Pour une segmentation, la transformation spatiale doit aussi s’appliquer à la cible.

QUESTION À POSER
Pourquoi ne pas répartir des augmentations d’une même image entre train et test ?

RÉPONSE ATTENDUE
Cela crée une dépendance et une fuite entre les partitions.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 73. LE JEU DE DONNÉES FAIT PARTIE DU MODÈLE

DIAPOSITIVE 73 — LE JEU DE DONNÉES FAIT PARTIE DU MODÈLE

EXPLICATION TECHNIQUE
Le jeu digits de scikit-learn contient 1797 images 8×8 de dix classes, avec des niveaux de gris entre 0 et 16. Cette petite base permet des expériences CPU rapides, mais ne représente pas les contraintes de la vision en conditions réelles. Une séparation stratifiée conserve approximativement les proportions de classes, sans garantir une séparation par auteur des chiffres : les notebooks ne disposent pas d'identifiants permettant un audit complet de ce niveau. Les conclusions doivent donc porter sur le protocole présenté. Pour un projet réel, l'unité de séparation doit suivre le scénario de déploiement.

QUESTION À POSER
Une séparation stratifiée empêche-t-elle toutes les fuites ?

RÉPONSE ATTENDUE
Non : elle ne traite ni les doublons ni les dépendances entre sujets.

LECTURES ET RÉFÉRENCES
scikit-learn — Jeu de données digits
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

Geoffrey Daniel — Réseaux de neurones et deep learning : utilisation et méthodologie
https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf

## 74. TRAIN, VALIDATION ET TEST : QUI DÉCIDE ?

Partition | Utilisation | À éviter
Train | Poids et statistiques apprises | Information issue du test
Validation | Modèle, hyperparamètres et checkpoint | Confondre sélection et estimation finale
Test | Évaluer la procédure déjà choisie | Choisir les réglages selon son score
Nouvelle distribution | Vérifier le transfert externe | La remplacer par le seul test interne

DIAPOSITIVE 74 — TRAIN, VALIDATION ET TEST : QUI DÉCIDE ?

EXPLICATION TECHNIQUE
Expliquer la séparation comme une gestion des décisions. Le train détermine les poids et, si nécessaire, les paramètres du prétraitement. La validation guide le choix de l'architecture, des hyperparamètres et du checkpoint. Le test intervient une fois le protocole de choix terminé. Il n'est pas interdit de constater qu'un score test est faible ; ce qui est problématique est de continuer à l'optimiser en prétendant conserver une estimation indépendante. Si le protocole est modifié après l'observation du test, il faut une nouvelle évaluation indépendante pour une affirmation forte.

QUESTION À POSER
Peut-on ajuster la normalisation sur l’ensemble des images ?

RÉPONSE ATTENDUE
Pas si elle apprend des statistiques : l’ajustement doit être limité au train.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 75. MÉTRIQUES ET MATRICE DE CONFUSION

DIAPOSITIVE 75 — MÉTRIQUES ET MATRICE DE CONFUSION

EXPLICATION TECHNIQUE
Pour une classe donnée, considérer cette classe comme positive et toutes les autres comme négatives. Dans la matrice de confusion des notebooks, les lignes sont les vraies classes et les colonnes les prédictions ; annoncer cette convention. Une classe rare peut avoir un rappel faible tout en contribuant peu à l'accuracy globale. Le macro-F1 moyenne les F1 calculés séparément par classe ; ce n'est pas le F1 calculé à partir d'une précision macro et d'un rappel macro. Prévoir une convention lorsque le dénominateur est nul et afficher les effectifs pour contextualiser les métriques.

ÉQUATION — SOURCE LATEX
\operatorname{precision}=\frac{TP}{TP+FP},\quad\operatorname{rappel}=\frac{TP}{TP+FN},\quad F_1=\frac{2PR}{P+R}

LECTURE À VOIX HAUTE
« La précision vaut le nombre de vrais positifs divisé par le nombre de prédictions positives, soit vrais positifs plus faux positifs. »
« Le rappel vaut les vrais positifs divisés par vrais positifs plus faux négatifs. »
« F un vaut deux fois P fois R, divisé par P plus R. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `TP` | « vrais positifs, ou té pé » | Exemples de la classe positive prédits positifs. |
| `FP` | « faux positifs, ou effe pé » | Exemples négatifs prédits positifs. |
| `FN` | « faux négatifs, ou effe enne » | Exemples positifs prédits négatifs. |
| `P` | « pé » | Précision : fraction des prédictions positives qui sont correctes. |
| `R` | « erre » | Rappel : fraction des positifs réels qui sont retrouvés. |
| `F_1` | « effe un » | Moyenne harmonique de la précision et du rappel. |
| `2PR/(P+R)` | « deux pé erre divisé par pé plus erre » | Formule de la moyenne harmonique pour deux valeurs. |

INTERPRÉTATION
La précision décrit la fiabilité des alertes positives. Le rappel décrit la couverture des vrais positifs.

POINT D’ATTENTION
Ces formules concernent une classe positive définie. Si un dénominateur est nul, la convention de calcul doit être précisée. En multiclasse, indiquer aussi le type de moyenne.

QUESTION À POSER
Le macro-F1 est-il le F1 de la précision et du rappel moyens ?

RÉPONSE ATTENDUE
Non : il moyenne les F1 calculés classe par classe.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 76. TRANSFERT : RÉUTILISER UNE REPRÉSENTATION

DIAPOSITIVE 76 — TRANSFERT : RÉUTILISER UNE REPRÉSENTATION

EXPLICATION TECHNIQUE
Séparer backbone et tête dans l'équation. Les poids du backbone contiennent une représentation issue d'un entraînement antérieur ; ils ne sont pas universellement pertinents. Dans le TP, la source contient les chiffres 0 à 4 et la cible les chiffres 5 à 9. Les espaces d'étiquettes sont disjoints, mais le type d'image reste proche. C'est un transfert pédagogique contrôlé, distinct d'un réseau préentraîné sur ImageNet. Le coût de préentraînement source doit être annoncé quand on compare les budgets, même s'il est partagé entre plusieurs tâches cibles.

ÉQUATION — SOURCE LATEX
f(x)=h_{\psi}(g_{\phi}(x)),\qquad\phi\leftarrow\phi_{\rm source},\quad\psi\leftarrow\psi_{\rm nouvelle}

LECTURE À VOIX HAUTE
« f de x vaut h psi appliquée à g phi de x. »
« On initialise phi avec les paramètres source et psi avec de nouveaux paramètres. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `f(x)` | « effe de x » | Modèle complet appliqué à l’entrée. |
| `g_\phi(x)` | « gé paramétré par phi, appliqué à x » | Extracteur de caractéristiques, ou backbone. |
| `h_\psi` | « ache paramétré par psi » | Tête qui transforme les caractéristiques en prédiction. |
| `\phi,\ \psi` | « phi, psi » | Paramètres de l’extracteur et paramètres de la tête. |
| `\leftarrow` | « reçoit, ou est initialisé avec » | Affectation d’une valeur, pas une égalité à démontrer. |
| `\phi_{\rm source}` | « phi source » | Paramètres provenant d’un entraînement antérieur. |
| `\psi_{\rm nouvelle}` | « psi nouvelle » | Paramètres d’une tête adaptée à la nouvelle tâche. |

INTERPRÉTATION
Le transfert réutilise un extracteur et lui associe une tête correspondant à la tâche cible.

POINT D’ATTENTION
Dans cette formule, phi et psi sont des ensembles de paramètres. Le rôle de g et h diffère de la notation de l’introduction : il faut toujours relire les définitions locales.

QUESTION À POSER
Pourquoi remplacer la dernière couche ?

RÉPONSE ATTENDUE
Parce que les classes et éventuellement le nombre de sorties de la cible changent.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 77. TROIS STRATÉGIES DE TRANSFERT

Stratégie | Backbone | Tête | Usage / limite
Depuis zéro | Aléatoire, entraîné | Entraînée | Référence de comparaison
Features gelées | Source, figé | Entraînée | Peu de labels, capacité d’adaptation limitée
Fine-tuning | Source, adapté | Entraînée | Plus flexible, risque de surapprentissage

DIAPOSITIVE 77 — TROIS STRATÉGIES DE TRANSFERT

EXPLICATION TECHNIQUE
Comparer les procédures à données et partition identiques. L'extraction de caractéristiques apprend seulement la tête ; elle économise le passage arrière du backbone et limite la flexibilité. Le fine-tuning part d'un état source mais adapte une partie ou la totalité du réseau avec un taux contrôlé. L'entraînement depuis zéro fournit une référence indispensable. Un transfert peut être négatif si la représentation source ou le protocole est mal adapté. Dans le TP, le budget cible est annoncé et le coût source présenté séparément ; le test n'est pas utilisé pour décider laquelle des stratégies conserver.

QUESTION À POSER
Quelle baseline permet de détecter un transfert négatif ?

RÉPONSE ATTENDUE
Le même modèle entraîné depuis zéro avec un protocole comparable.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 78. FINE-TUNING : UNE PROCÉDURE EXPLICITE

DIAPOSITIVE 78 — FINE-TUNING : UNE PROCÉDURE EXPLICITE

EXPLICATION TECHNIQUE
Une phase de tête seule peut éviter que des gradients provenant d'une tête aléatoire perturbent immédiatement la représentation source. Après le dégel, il faut reconstruire l'optimiseur ou lui ajouter les nouveaux paramètres si ceux-ci n'étaient pas inclus. Des groupes de paramètres autorisent un taux différent pour la tête et pour le backbone. Aucune séquence de phases ne garantit un gain ; c'est une procédure à tester et à comparer. Si l'on change de domaine ou de prétraitement, vérifier aussi la distribution des activations et les statistiques des couches de normalisation.

QUESTION À POSER
Que faut-il vérifier dans l’optimiseur après un dégel ?

RÉPONSE ATTENDUE
Que les paramètres nouvellement entraînables font partie de ses groupes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 79. GEL DES POIDS ET MODE ÉVALUATION

DIAPOSITIVE 79 — GEL DES POIDS ET MODE ÉVALUATION

EXPLICATION TECHNIQUE
Ces deux commandes répondent à des questions différentes. Un backbone peut être figé du point de vue des poids tout en mettant à jour les buffers BatchNorm si son mode reste train. Inversement, eval ne bloque pas les gradients d'un paramètre qui les requiert. Dans notre petit CNN, il n'y a ni BatchNorm ni Dropout ; cela isole le mécanisme de transfert. Pour un ResNet importé, ce détail devient essentiel. Faire vérifier les drapeaux requires_grad, l'appartenance aux groupes d'optimiseur et l'évolution des buffers avant et après une époque.

QUESTION À POSER
Pourquoi un backbone sans mise à jour de poids peut-il produire des sorties différentes ?

RÉPONSE ATTENDUE
Le dropout et les statistiques de BatchNorm peuvent encore changer.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 80. UTILISER UN MODÈLE PRÉENTRAÎNÉ PUBLIC

DIAPOSITIVE 80 — UTILISER UN MODÈLE PRÉENTRAÎNÉ PUBLIC

EXPLICATION TECHNIQUE
Ce bloc est une extension de lecture, distincte du TP CPU sans téléchargement. Avec Torchvision, l'objet weights expose les transformations attendues : redimensionnement, recadrage et normalisation. Les images doivent avoir un nombre de canaux adapté, et l'ordre des classes de la tête source n'est plus valable lorsque l'on remplace celle-ci. Le téléchargement de poids nécessite un accès réseau. L'extrait ne constitue pas un entraînement complet ni une démonstration de performance. Le notebook principal montre le même mécanisme de séparation backbone-tête à partir d'un préentraînement source réalisé localement.

QUESTION À POSER
Pourquoi conserver le prétraitement associé aux poids ?

RÉPONSE ATTENDUE
La distribution d’entrée fait partie des hypothèses du préentraînement.

LECTURES ET RÉFÉRENCES
Torchvision 0.23 — ResNet18
https://docs.pytorch.org/vision/0.23/models/generated/torchvision.models.resnet18.html

## 81. COMPARER DES EXPÉRIENCES

À conserver | Pourquoi
Split et graine | Comparer sur les mêmes observations
Architecture et paramètres | Identifier la capacité entraînée
Optimiseur, pas et batch | Reproduire le budget d’apprentissage
Critère de checkpoint | Comprendre la sélection
Score, effectifs et temps | Interpréter performance et coût

DIAPOSITIVE 81 — COMPARER DES EXPÉRIENCES

EXPLICATION TECHNIQUE
Un tableau d'expériences doit permettre de reconstruire les décisions. En plus du score, conserver la graine, le découpage, la configuration, le nombre de mises à jour et le temps mesuré sur un matériel identifié. Une comparaison à une seule graine reste indicative. Les ablations changent un facteur à la fois lorsque l'objectif est d'isoler son effet ; si plusieurs facteurs changent, le résultat concerne une recette complète. Les coûts source et cible du transfert doivent être distingués. Une expérience terminée avec une précision faible peut être pédagogiquement utile si elle est documentée et correctement interprétée.

QUESTION À POSER
Peut-on attribuer un gain au dropout si l’on a aussi changé la largeur ?

RÉPONSE ATTENDUE
Non, pas sans expérience supplémentaire isolant les effets.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 82. ANALYSE D’ERREURS : REGARDER LES EXEMPLES

DIAPOSITIVE 82 — ANALYSE D’ERREURS : REGARDER LES EXEMPLES

EXPLICATION TECHNIQUE
Le score global masque des mécanismes très différents : une classe peut être sous-représentée, une annotation erronée ou un exemple simplement ambigu à faible résolution. Afficher ensemble vérité, prédiction et confiance, sans prendre cette confiance pour une probabilité calibrée. Construire une hypothèse d'erreur puis une vérification ciblée. Si l'analyse du test guide une modification du modèle, le test a servi au développement et ne doit plus être présenté comme une estimation indépendante de cette nouvelle version. Les notebooks emploient la validation pour l'investigation et réservent le test au bilan final.

QUESTION À POSER
Quel risque présente l’inspection répétée du test pour améliorer le modèle ?

RÉPONSE ATTENDUE
Le test devient progressivement un outil de sélection.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 83. TP 03 · MESURER LE TRANSFERT

DIAPOSITIVE 83 — TP 03 · MESURER LE TRANSFERT

EXPLICATION TECHNIQUE
Répartition : 25 minutes de préparation, 35 minutes d'apprentissage source, 55 minutes de comparaison des trois stratégies, 35 minutes d'analyse et 30 minutes de restitution. Les étiquettes cible sont remappées de 5–9 vers 0–4 pour la nouvelle tête à cinq sorties. Les données source et cible sont séparées par classe ; aucune image cible n'est utilisée pour apprendre la source. Chaque stratégie choisit son checkpoint sur la validation. Le test compare des procédures fixées à l'avance. Un score moins bon après transfert constitue un résultat à expliquer, pas une raison de modifier le test.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Un tableau des trois protocoles, leur coût et une interprétation du transfert positif ou négatif.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 84. JOUR 3 · À RETENIR

DIAPOSITIVE 84 — JOUR 3 · À RETENIR

EXPLICATION TECHNIQUE
Faire conclure chaque binôme avec trois phrases : quelle configuration a été comparée, quelle observation a été faite sur la validation, et quelle explication reste une hypothèse. Revenir sur la taille du domaine source et sur le nombre réduit de labels cible. Les résultats du petit jeu ne permettent pas d'affirmer qu'une famille d'architectures domine universellement. Préparer la transition : les CNN mélangent localement l'information avec des poids indépendants de l'exemple ; l'attention calculera une pondération entre éléments dépendant du contenu observé.

QUESTION À POSER
Qu’apportera l’attention par rapport à une convolution locale ?

RÉPONSE ATTENDUE
Un mélange entre positions dont les poids dépendent du contenu.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 85. ATTENTION ET TRANSFORMERS

DIAPOSITIVE 85 — ATTENTION ET TRANSFORMERS

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 86. JOUR 4 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Séquences | Représentation, récurrence et positions | 60
Attention | Q, K, V, softmax et masques | 90
Architecture | Têtes, normalisation et blocs Transformers | 90
TP 04 | Calcul d’attention et tests de causalité | 150
Synthèse | Dimensions, coût et questions de contrôle | 30

DIAPOSITIVE 86 — JOUR 4 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 87. UNE SÉQUENCE COMME TENSEUR

DIAPOSITIVE 87 — UNE SÉQUENCE COMME TENSEUR

EXPLICATION TECHNIQUE
Donner plusieurs exemples de tokens : sous-mots en texte, instants d'une série temporelle ou patches d'une image. Le vocabulaire et la tokenisation déterminent l'espace d'entrée ; des modèles avec des tokenisations différentes ne sont pas comparables directement par la seule perplexité. Les séquences peuvent avoir des longueurs variées. Le padding est une commodité de calcul, pas une observation : il doit être exclu de l'attention et, selon la tâche, de la perte. Distinguer la dimension d d'une représentation continue et la taille V du vocabulaire d'identifiants discrets.

ÉQUATION — SOURCE LATEX
X\in\mathbb R^{B\times n\times d}

LECTURE À VOIX HAUTE
« Grand X appartient à l’espace des tenseurs réels de taille B par n par d. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X` | « grand x » | Tenseur représentant un batch de séquences. |
| `\in` | « appartient à » | Indique le type d’objet mathématique. |
| `\mathbb R` | « erre, ensemble des réels » | Les composantes du tenseur sont des nombres réels. |
| `B` | « bé » | Nombre de séquences dans le batch. |
| `n` | « enne » | Nombre de positions dans une séquence, avec padding éventuel. |
| `d` | « dé » | Nombre de caractéristiques par position. |
| `B\times n\times d` | « bé par enne par dé » | Tailles des trois axes, dans cet ordre. |

INTERPRÉTATION
Pour chaque séquence et chaque position, le modèle manipule un vecteur de d nombres.

POINT D’ATTENTION
Le produit B fois n fois d donne le nombre total de valeurs, mais la forme du tenseur garde l’ordre et le rôle de ses axes.

QUESTION À POSER
Un token correspond-il toujours à un mot complet ?

RÉPONSE ATTENDUE
Non : il peut représenter un sous-mot, un caractère, un patch ou un autre élément.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 88. RÉCURRENCE ET DÉPENDANCES LONGUES

DIAPOSITIVE 88 — RÉCURRENCE ET DÉPENDANCES LONGUES

EXPLICATION TECHNIQUE
Cette parenthèse explique la motivation historique, sans prétendre que la récurrence est obsolète. Un RNN partage ses poids dans le temps et condense le passé dans un état. Les gradients sur de longues distances impliquent de nombreux produits de Jacobiennes. Des mécanismes comme LSTM et GRU ont été conçus pour améliorer cette dynamique. L'attention introduit un chemin direct entre positions, au prix d'un calcul potentiellement quadratique. Des architectures récurrentes ou à état restent pertinentes lorsque le coût mémoire ou la structure du flux les favorise.

ÉQUATION — SOURCE LATEX
h_t=\phi(W_xx_t+W_hh_{t-1}+b)

LECTURE À VOIX HAUTE
« h t vaut phi appliquée à W x fois x t, plus W h fois h t moins un, plus b. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `t` | « té » | Position courante dans la séquence. |
| `x_t` | « x indice t » | Vecteur d’entrée à la position t. |
| `h_t,\ h_{t-1}` | « ache t, ache t moins un » | État caché courant et état caché précédent. |
| `W_x` | « w indice x » | Matrice qui transforme l’entrée courante. |
| `W_h` | « w indice ache » | Matrice qui transforme l’état précédent. |
| `b` | « bé » | Biais du calcul de l’état. |
| `\phi` | « phi » | Activation appliquée composante par composante. |
| `W_xx_t+W_hh_{t-1}+b` | « W x fois x t, plus W h fois h t moins un, plus b » | Combinaison de l’information nouvelle et de l’état mémorisé. |

INTERPRÉTATION
L’état courant dépend à la fois du token actuel et du résumé calculé au pas précédent.

POINT D’ATTENTION
Les mêmes matrices sont partagées entre les positions. Les indices x et h nomment le rôle des matrices, ils ne sont pas des variables qui multiplient W.

QUESTION À POSER
Quel compromis apparaît avec des interactions entre toutes les positions ?

RÉPONSE ATTENDUE
Un chemin plus direct, mais davantage de calcul et de mémoire selon l’implémentation.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 89. EMBEDDINGS : DES IDENTIFIANTS AUX VECTEURS

DIAPOSITIVE 89 — EMBEDDINGS : DES IDENTIFIANTS AUX VECTEURS

EXPLICATION TECHNIQUE
Une entrée entière n'est pas une grandeur ordinale : l'identifiant 8 n'est pas intrinsèquement plus proche de 9 que de 2. L'embedding transforme cet index en vecteur continu. Sa table comporte V×d paramètres, ce qui peut devenir coûteux pour un grand vocabulaire. Seules les lignes utilisées contribuent directement à une étape donnée, selon le calcul et l'optimiseur. La proximité géométrique des vecteurs est une conséquence de l'objectif appris et ne garantit pas une relation sémantique précise. Pour le mini-Transformer, les tokens sont volontairement de petits symboles entiers afin d'isoler le mécanisme.

ÉQUATION — SOURCE LATEX
E\in\mathbb R^{V\times d},\qquad x_t=E[\operatorname{id}(t),:]

LECTURE À VOIX HAUTE
« E est une matrice réelle à V lignes et d colonnes. »
« x t est la ligne de E correspondant à l’identifiant du token présent à la position t, en prenant toutes ses colonnes. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `E` | « e majuscule » | Table d’embeddings apprise. |
| `V` | « vé majuscule » | Nombre de tokens du vocabulaire. |
| `d` | « dé » | Dimension de chaque embedding. |
| `\mathbb R^{V\times d}` | « matrices réelles à V lignes et d colonnes » | Une ligne par token et une colonne par caractéristique. |
| `t` | « té » | Position du token dans la séquence. |
| `\operatorname{id}(t)` | « identifiant du token à la position t » | Dans cette écriture, index de la ligne qui correspond au token observé. |
| `E[\operatorname{id}(t),:]` | « E, ligne identifiant du token t, toutes les colonnes » | Sélection d’une ligne de la table. |
| `x_t` | « x indice t » | Vecteur d’embedding renvoyé à cette position. |
| ` : ` | « deux-points, toutes les colonnes » | Notation d’indexation qui sélectionne toutes les caractéristiques. |

INTERPRÉTATION
Une consultation de table remplace un identifiant discret par un vecteur continu.

POINT D’ATTENTION
L’identifiant du token n’est pas son numéro de position. V majuscule est ici la taille du vocabulaire, alors qu’il désigne les valeurs dans l’attention.

QUESTION À POSER
Combien de paramètres pour V=1000 et d=64 ?

RÉPONSE ATTENDUE
64 000, sans biais.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 90. INFORMATION DE POSITION

DIAPOSITIVE 90 — INFORMATION DE POSITION

EXPLICATION TECHNIQUE
La propriété de permutation concerne une auto-attention sans masque positionnel et avec les mêmes projections à toutes les positions. Un masque causal introduit déjà une structure d'ordre, mais ne remplace pas toutes les informations de position utiles. Dans le notebook, une table de positions apprises est ajoutée à chaque embedding avant les blocs. Cela fixe une longueur maximale prévue et ne garantit pas une extrapolation à des positions jamais vues. Les encodages relatifs et rotatifs constituent d'autres choix, seulement mentionnés ici pour situer cette famille de solutions.

ÉQUATION — SOURCE LATEX
X_0=E[\text{tokens}]+P,\qquad\operatorname{SA}(\Pi X)=\Pi\operatorname{SA}(X)

LECTURE À VOIX HAUTE
« X zéro vaut les embeddings des tokens, plus leurs représentations de position P. »
« Sans information ni masque de position, l’auto-attention appliquée à X dont on a permuté les lignes donne la même permutation des sorties de l’auto-attention. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X_0` | « x indice zéro » | Représentations à l’entrée de la première couche Transformer. |
| `E[\text{tokens}]` | « embeddings des tokens » | Lignes de la table d’embeddings sélectionnées pour la séquence. |
| `P` | « pé majuscule » | Matrice d’informations de position, compatible avec la forme des embeddings. |
| `+` | « plus » | Addition composante par composante des contenus et des positions. |
| `\operatorname{SA}` | « auto-attention, ou self-attention » | Opération d’attention où les requêtes, clés et valeurs proviennent de la même séquence. |
| `\Pi` | « pi majuscule » | Matrice qui permute l’ordre des lignes. |
| `\Pi X` | « pi appliquée à X » | Séquence dont les positions ont été réordonnées. |
| `\Pi\operatorname{SA}(X)` | « pi appliquée aux sorties de l’auto-attention » | Même permutation appliquée aux vecteurs de sortie. |

INTERPRÉTATION
La deuxième égalité exprime l’équivariance par permutation de l’auto-attention dépourvue de structure positionnelle.

POINT D’ATTENTION
Pi majuscule est ici une matrice de permutation, pas le produit de plusieurs termes. L’égalité suppose notamment l’absence de masque positionnel et des projections partagées.

QUESTION À POSER
Que signifie l’équivariance par permutation de l’auto-attention non masquée ?

RÉPONSE ATTENDUE
Permuter les tokens permute les sorties correspondantes.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 91. ENCODAGE SINUSOÏDAL DES POSITIONS

DIAPOSITIVE 91 — ENCODAGE SINUSOÏDAL DES POSITIONS

EXPLICATION TECHNIQUE
Décrire t comme la position et i comme un index de paire de caractéristiques. Les fréquences réparties sur plusieurs échelles rendent les positions distinguables dans différents régimes. Pour un décalage donné, les formules trigonométriques relient les sinus et cosinus de positions voisines par une transformation linéaire dans chaque paire. Cela motive l'approche sans prouver qu'un modèle entraîné sur une longueur donnée fonctionnera arbitrairement loin. Comparer avec la table apprise du TP : moins de structure imposée mais aucune valeur apprise au-delà des indices disponibles.

ÉQUATION — SOURCE LATEX
PE_{t,2i}=\sin\!\left(\frac{t}{10000^{2i/d}}\right),\qquad PE_{t,2i+1}=\cos\!\left(\frac{t}{10000^{2i/d}}\right)

LECTURE À VOIX HAUTE
« P E, à la position t et à la coordonnée deux i, vaut le sinus de t divisé par dix mille à la puissance deux i sur d. »
« P E, à la position t et à la coordonnée deux i plus un, vaut le cosinus du même quotient. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `PE_{t,2i}` | « P E indice t, deux i » | Valeur de l’encodage de position pour le token de position t, sur la coordonnée paire 2i. |
| `PE_{t,2i+1}` | « P E indice t, deux i plus un » | Valeur sur la coordonnée impaire associée. |
| `t` | « té » | Position du token dans la séquence, en commençant ici à zéro. |
| `i` | « i » | Indice d’une paire de coordonnées ; ce n’est pas l’indice d’un token. |
| `d` | « dé » | Dimension de la représentation du token ; on suppose ici d pair. |
| `2i,\ 2i+1` | « deux i ; deux i plus un » | Deux coordonnées consécutives : une paire sinus/cosinus. |
| `\sin,\ \cos` | « sinus ; cosinus » | Fonctions trigonométriques dont les arguments sont exprimés en radians. |
| `10000^{2i/d}` | « dix mille puissance deux i sur d » | Facteur d’échelle qui varie selon la paire de coordonnées. Toute la fraction 2i/d est l’exposant. |
| `\frac{t}{10000^{2i/d}}` | « t divisé par dix mille puissance deux i sur d » | Argument des fonctions : il associe la position à plusieurs fréquences. |

INTERPRÉTATION
Chaque position reçoit un vecteur déterministe. Les différentes coordonnées évoluent à des fréquences différentes, ce qui fournit au réseau une information d’ordre.

POINT D’ATTENTION
Les indices t et 2i identifient une case du tableau PE ; ce ne sont pas des puissances. La constante 10000 fixe une gamme de fréquences et n’est ni le nombre de tokens ni une probabilité.

QUESTION À POSER
L’encodage sinusoidal contient-il des paramètres entraînables ?

RÉPONSE ATTENDUE
Pas dans sa forme déterministe standard.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 92. L’ATTENTION COMME SOMME PONDÉRÉE

DIAPOSITIVE 92 — L’ATTENTION COMME SOMME PONDÉRÉE

EXPLICATION TECHNIQUE
Cette écriture suffit à expliquer le mécanisme sans métaphore obligatoire. La requête détermine ce que la position i cherche ; la clé fournit un espace de comparaison ; la valeur porte l'information mélangée dans la sortie. Les clés et les valeurs peuvent avoir des dimensions différentes, mais la dimension des requêtes doit correspondre à celle des clés pour un produit scalaire. Avec softmax, la sortie avant projection est dans l'enveloppe convexe des valeurs. Cela n'implique pas que le bloc complet soit une simple moyenne, puisqu'il comprend des projections, des résidus et des non-linéarités.

ÉQUATION — SOURCE LATEX
o_i=\sum_{j=1}^{n_k}\alpha_{ij}v_j,\qquad\sum_j\alpha_{ij}=1,\quad\alpha_{ij}\ge0

LECTURE À VOIX HAUTE
« o indice i est égal à la somme, pour j allant de un à n indice k, de alpha indice i j multiplié par v indice j. »
« Pour une requête i fixée, la somme des alpha i j sur les clés j vaut un, et chaque alpha i j est positif ou nul. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `o_i` | « o indice i » | Vecteur de sortie de l’attention pour la requête i. |
| `i` | « i » | Indice de la requête dont on calcule la représentation. |
| `j` | « ji » | Indice d’une clé et du vecteur de valeur associé. |
| `n_k` | « n indice k » | Nombre de clés et de valeurs disponibles. |
| `\sum_{j=1}^{n_k}` | « somme pour j de un à n indice k » | Addition de la contribution de chaque valeur. |
| `\alpha_{ij}` | « alpha indice i j » | Poids scalaire donné par la requête i à la valeur j. |
| `v_j` | « vé indice j » | Vecteur de valeur associé à la clé j. |
| `\alpha_{ij}v_j` | « alpha i j fois v j » | Multiplication de toutes les composantes de v_j par le même poids. |
| `\sum_j\alpha_{ij}=1` | « la somme des alpha i j sur j vaut un » | Normalisation des poids d’une même requête. |
| `\alpha_{ij}\ge0` | « alpha i j est supérieur ou égal à zéro » | Les poids sont non négatifs. |

INTERPRÉTATION
L’attention construit chaque sortie comme une moyenne pondérée des valeurs. Les poids changent avec la requête : deux tokens peuvent agréger différemment les mêmes valeurs.

POINT D’ATTENTION
La somme égale à un décrit les poids après softmax et avant un éventuel dropout d’attention. Un poids élevé indique une contribution à cette agrégation ; il ne constitue pas, à lui seul, une explication causale de la prédiction.

QUESTION À POSER
Sur quel axe les poids doivent-ils sommer à un ?

RÉPONSE ATTENDUE
Sur l’axe des clés consultées par chaque requête.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 93. Q, K, V : PROJECTIONS APPRISES

DIAPOSITIVE 93 — Q, K, V : PROJECTIONS APPRISES

EXPLICATION TECHNIQUE
Ici, X a n lignes et d colonnes, en omettant le batch. Les matrices W ont donc l'orientation entrée×sortie, contrairement à la convention de stockage de nn.Linear exposée plus tôt. Le calcul reste identique : une bibliothèque stockant sortie×entrée applique la transposée. Q et K ont n×d_k éléments, V en a n×d_v. Les trois matrices sont différentes en général, même si leur entrée est commune. Le gradient traverse à la fois les valeurs et les scores qui règlent leur mélange ; l'attention est entraînée de bout en bout.

ÉQUATION — SOURCE LATEX
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V\\W_Q,W_K\in\mathbb R^{d\times d_k},\quad W_V\in\mathbb R^{d\times d_v}

LECTURE À VOIX HAUTE
« Q vaut X fois W indice Q ; K vaut X fois W indice K ; V vaut X fois W indice V. »
« W Q et W K appartiennent à l’espace des matrices réelles de dimension d par d indice k ; W V appartient à l’espace des matrices réelles de dimension d par d indice v. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X` | « iks » | Matrice d’entrée de taille n × d : une ligne par token. La dimension de batch est omise. |
| `Q,\ K,\ V` | « ku, ka, vé » | Matrices des requêtes, clés et valeurs. Leurs tailles sont n × d_k, n × d_k et n × d_v. |
| `W_Q,\ W_K,\ W_V` | « double vé indice Q, K, V » | Trois matrices de paramètres appris qui projettent les mêmes entrées vers trois rôles. |
| `XW_Q` | « X fois W Q » | Produit matriciel, pas multiplication composante par composante. |
| `d` | « dé » | Dimension des représentations d’entrée. |
| `d_k,\ d_v` | « d indice k ; d indice v » | Dimensions respectives des requêtes/clés et des valeurs pour cette tête. |
| `\in` | « appartient à » | Indique le type et la dimension d’un objet. |
| `\mathbb R^{d\times d_k}` | « espace des matrices réelles d par d k » | Matrices à d lignes et d_k colonnes ; le symbole × sépare ici des dimensions. |

INTERPRÉTATION
Les requêtes servent à chercher, les clés à mesurer la compatibilité et les valeurs à fournir le contenu agrégé. Ce sont trois transformations apprises, pas trois copies nécessairement identiques.

POINT D’ATTENTION
Q et K doivent avoir la même largeur pour calculer leurs produits scalaires. La largeur d_v des valeurs peut être différente. Les biais sont omis dans cette écriture simplifiée.

QUESTION À POSER
Q=K=V dans une auto-attention ?

RÉPONSE ATTENDUE
Pas en général : l’entrée est commune, les projections apprises sont distinctes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 94. SCORES D’ATTENTION : TOUTES LES PAIRES

DIAPOSITIVE 94 — SCORES D’ATTENTION : TOUTES LES PAIRES

EXPLICATION TECHNIQUE
Écrire explicitement un produit scalaire entre une ligne de Q et une ligne de K. La transposition de K permet de calculer tous ces produits en une seule opération. Les lignes n'ont pas besoin d'avoir la même longueur en cross-attention : n_q peut être la longueur cible et n_k la longueur source. La largeur d_k doit en revanche être la même pour les deux. Le facteur racine carrée sera justifié ensuite. Une carte de scores brute n'est pas encore une carte de probabilités : ses valeurs peuvent être positives ou négatives et leur somme est quelconque.

ÉQUATION — SOURCE LATEX
S=\frac{QK^\top}{\sqrt{d_k}},\qquad S_{ij}=\frac{q_i^\top k_j}{\sqrt{d_k}}

LECTURE À VOIX HAUTE
« S vaut Q multiplié par K transposée, le tout divisé par la racine carrée de d indice k. »
« Le score S indice i j vaut le produit scalaire de q indice i et k indice j, divisé par la racine carrée de d indice k. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `S` | « esse » | Matrice des scores, de taille n_q × n_k. |
| `S_{ij}` | « esse indice i j » | Score entre la requête i et la clé j. |
| `Q,\ K` | « ku ; ka » | Matrices des requêtes et des clés, de tailles n_q × d_k et n_k × d_k. |
| `{}^\top` | « transposée » | Échange les lignes et les colonnes ; ce symbole n’est pas un exposant numérique. |
| `QK^\top` | « Q fois K transposée » | Produit matriciel qui calcule tous les scores requête–clé. |
| `q_i,\ k_j` | « ku indice i ; ka indice j » | Vecteurs représentant une requête et une clé. Dans q_i^T k_j, on les écrit comme des vecteurs colonnes. |
| `q_i^\top k_j` | « q i transposée fois k j » | Produit scalaire : somme des produits de composantes correspondantes. |
| `d_k` | « d indice k » | Nombre de composantes d’une requête ou d’une clé. |
| `\sqrt{d_k}` | « racine carrée de d indice k » | Facteur qui contrôle l’échelle des scores. |

INTERPRÉTATION
Chaque ligne de S compare une requête avec toutes les clés. Le calcul matriciel rassemble ces comparaisons pour les effectuer efficacement en parallèle.

POINT D’ATTENTION
Un score peut être négatif ou supérieur à un : ce n’est pas encore une probabilité. Diviser par √d_k ne normalise pas q et k à une norme unitaire ; ce n’est donc pas un calcul de similarité cosinus.

QUESTION À POSER
Quelle est la forme si Q a 5 lignes et K en a 8 ?

RÉPONSE ATTENDUE
5 × 8, avec une largeur d_k commune.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 95. POURQUOI DIVISER PAR √dₖ ?

DIAPOSITIVE 95 — POURQUOI DIVISER PAR √dₖ ?

EXPLICATION TECHNIQUE
Annoncer les hypothèses : composantes centrées, indépendantes, de variance unité, avec indépendance appropriée entre q et k. Chaque produit q_r k_r a alors une variance d'ordre un et la variance de la somme est proportionnelle au nombre de termes. Les représentations réelles n'obéissent pas exactement à ces hypothèses ; il s'agit d'une justification d'échelle. Un softmax très concentré peut avoir de faibles dérivées pour de nombreuses directions. Le facteur ne normalise pas la norme exacte de chaque requête et ne transforme pas le produit scalaire en similarité cosinus.

ÉQUATION — SOURCE LATEX
\operatorname{Var}\!\left(\sum_{r=1}^{d_k}q_rk_r\right)\approx d_k\quad\Longrightarrow\quad\operatorname{Var}\!\left(\frac{q^\top k}{\sqrt{d_k}}\right)\approx1

LECTURE À VOIX HAUTE
« La variance de la somme, pour r de un à d indice k, des produits q indice r fois k indice r est approximativement égale à d indice k. »
« Par conséquent, la variance du produit scalaire q transposée fois k, divisé par la racine carrée de d indice k, est approximativement égale à un. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\operatorname{Var}` | « variance » | Mesure la dispersion d’une variable aléatoire autour de sa moyenne. |
| `r` | « erre » | Indice d’une composante des vecteurs q et k. |
| `d_k` | « d indice k » | Nombre de composantes additionnées dans le produit scalaire. |
| `q_r,\ k_r` | « ku indice r ; ka indice r » | Composantes aléatoires de la requête et de la clé. |
| `\sum_{r=1}^{d_k}q_rk_r` | « somme pour r de un à d k de q r fois k r » | Écriture développée du produit scalaire. |
| `q^\top k` | « q transposée fois k » | Même produit scalaire, en notation vectorielle. |
| `\approx` | « approximativement égal à » | Relation utilisée comme modèle de l’ordre de grandeur. |
| `\Longrightarrow` | « implique » ou « par conséquent » | Relie le constat sur la variance à l’effet de la mise à l’échelle. |
| `\sqrt{d_k}` | « racine carrée de d k » | Diviser la variable par √d_k divise sa variance par d_k. |

INTERPRÉTATION
Sous des hypothèses d’indépendance et de variance unitaire, additionner d_k produits donne une variance d_k. La mise à l’échelle réduit le risque de scores extrêmes qui satureraient le softmax.

POINT D’ATTENTION
Le raisonnement suppose notamment des composantes centrées, de variance unitaire, des requêtes et clés indépendantes dans ce modèle simplifié, et des termes non corrélés entre coordonnées. Ces conditions ne sont pas garanties exactement dans un réseau entraîné.

QUESTION À POSER
Le facteur 1/√dₖ réalise-t-il une normalisation cosinus ?

RÉPONSE ATTENDUE
Non : il ne divise pas par les normes individuelles de q et k.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 96. SOFTMAX PUIS AGRÉGATION DES VALEURS

DIAPOSITIVE 96 — SOFTMAX PUIS AGRÉGATION DES VALEURS

EXPLICATION TECHNIQUE
Montrer que multiplier une matrice n_q×n_k par n_k×d_v produit n_q×d_v. Chaque requête obtient sa propre combinaison de valeurs. La même clé peut contribuer fortement à plusieurs requêtes ; il n'y a pas de contrainte de somme un par colonne. Le mécanisme n'est donc pas un appariement exclusif. Pour un batch multi-têtes, les axes batch et tête sont indépendants et le softmax reste appliqué sur le dernier axe des clés. Une erreur d'axe peut produire des tenseurs de formes plausibles tout en changeant complètement l'opération.

ÉQUATION — SOURCE LATEX
A=\operatorname{softmax}_{\rm lignes}(S),\qquad O=AV\in\mathbb R^{n_q\times d_v}

LECTURE À VOIX HAUTE
« A vaut le softmax de S, appliqué ligne par ligne. »
« O vaut A fois V et appartient à l’espace des matrices réelles à n indice q lignes et d indice v colonnes. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `S` | « esse » | Matrice des scores, de taille n_q × n_k. |
| `\operatorname{softmax}_{\rm lignes}` | « softmax par lignes » | Transforme les scores d’une requête en poids normalisés sur toutes les clés. |
| `A` | « a majuscule » | Matrice des poids d’attention, de même taille que S. |
| `V` | « vé majuscule » | Matrice des valeurs, de taille n_k × d_v. |
| `O` | « o majuscule » | Matrice des sorties d’attention, de taille n_q × d_v. |
| `AV` | « A fois V » | Produit matriciel qui agrège les valeurs avec les poids d’attention. |
| `n_q,\ n_k` | « n indice q ; n indice k » | Nombres de requêtes et de clés. |
| `d_v` | « d indice v » | Dimension de chaque valeur et de chaque sortie pour cette tête. |
| `\in\mathbb R^{n_q\times d_v}` | « appartient à l’espace des matrices réelles n q par d v » | Indique le nombre de lignes et de colonnes de la sortie. |

INTERPRÉTATION
Le softmax choisit combien chaque valeur contribue. Le produit A V applique ensuite ces poids à toutes les composantes des valeurs. Les deux étapes séparent le choix des poids du contenu agrégé.

POINT D’ATTENTION
Le softmax se fait sur les clés, donc sur les colonnes de chaque ligne. Ici O est une matrice de sortie ; sur la slide de complexité, O(·) désignera une notation asymptotique sans rapport.

QUESTION À POSER
Les colonnes de A doivent-elles aussi sommer à un ?

RÉPONSE ATTENDUE
Non : seule chaque distribution sur les clés, donc chaque ligne, est normalisée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 97. ATTENTION : EXEMPLE NUMÉRIQUE COMPLET

DIAPOSITIVE 97 — ATTENTION : EXEMPLE NUMÉRIQUE COMPLET

EXPLICATION TECHNIQUE
Calculer les scores avant le softmax : les éléments diagonaux valent 1/racine(2) et les autres zéro. Le poids diagonal est exp(1/racine(2))/(exp(1/racine(2))+1), soit environ 0,6697615. Multiplier ensuite les poids de chaque ligne par V. La deuxième composante de la première sortie vaut deux fois 0,3302385, soit 0,660477. L'exemple volontairement petit montre que la sortie ne copie pas nécessairement un token unique. Le notebook refait le calcul en NumPy puis le compare à la version PyTorch, avec des assertions sur les valeurs et les sommes des lignes.

ÉQUATION — SOURCE LATEX
Q=K=\begin{bmatrix}1&0\\0&1\end{bmatrix},\quad V=\begin{bmatrix}1&0\\0&2\end{bmatrix}\\A\approx\begin{bmatrix}0.6698&0.3302\\0.3302&0.6698\end{bmatrix},\quad O\approx\begin{bmatrix}0.6698&0.6605\\0.3302&1.3395\end{bmatrix}

LECTURE À VOIX HAUTE
« Q et K sont égales à la matrice à deux lignes : première ligne, un puis zéro ; deuxième ligne, zéro puis un. V a pour première ligne un puis zéro, et pour deuxième ligne zéro puis deux. »
« A vaut approximativement : première ligne, zéro virgule six six neuf huit, puis zéro virgule trois trois zéro deux ; deuxième ligne, zéro virgule trois trois zéro deux, puis zéro virgule six six neuf huit. »
« O vaut approximativement : première ligne, zéro virgule six six neuf huit, puis zéro virgule six six zéro cinq ; deuxième ligne, zéro virgule trois trois zéro deux, puis un virgule trois trois neuf cinq. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `Q=K` | « Q égale K » | Dans cet exemple particulier, les deux matrices sont choisies identiques. |
| `\begin{bmatrix}1&0\\0&1\end{bmatrix}` | « matrice identité de taille deux » | Deux lignes et deux colonnes ; chaque ligne est un vecteur de requête ou de clé. |
| `V` | « vé » | Les valeurs sont (1, 0) et (0, 2), ce qui rend visible leur mélange. |
| `d_k=2` | « d indice k vaut deux » | Les scores sont divisés par √2 avant softmax. |
| `A` | « a majuscule » | Poids obtenus par softmax sur chaque ligne de QK^T/√2. |
| `O=AV` | « O égale A fois V » | Sorties calculées à partir des poids et des valeurs. |
| `\approx` | « approximativement égal à » | Les nombres affichés sont arrondis à quatre décimales. |
| `0.6698,\ 0.3302` | « zéro virgule six six neuf huit ; zéro virgule trois trois zéro deux » | Poids arrondis d’une ligne. Les décimales du support utilisent le point de la notation informatique. |

INTERPRÉTATION
Les scores diagonaux valent 1/√2 et les autres zéro. Pour la première requête, le premier poids vaut exp(1/√2)/(exp(1/√2)+1), soit environ 0,6697615. La première sortie est donc (0,6697615 ; 2 × 0,3302385), soit environ (0,6698 ; 0,6605).

POINT D’ATTENTION
Les lignes de A somment à un ; celles de O n’ont aucune raison de sommer à un. Calculer avec les valeurs non arrondies puis arrondir le résultat évite de petits écarts de dernière décimale.

QUESTION À POSER
Pourquoi la seconde coordonnée de O₁ vaut-elle environ 0,6605 ?

RÉPONSE ATTENDUE
La seconde valeur contient 2, pondéré par environ 0,3302.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 98. MASQUE CAUSAL ET MASQUE DE PADDING

DIAPOSITIVE 98 — MASQUE CAUSAL ET MASQUE DE PADDING

EXPLICATION TECHNIQUE
Distinguer l'information temporelle interdite de l'information absente. Une ligne entièrement masquée peut produire des NaN : il faut garantir au moins une clé accessible pour chaque requête effectivement évaluée. Les requêtes correspondant au padding doivent être exclues de la perte ou de l'agrégation finale selon la tâche. Les conventions booléennes des API peuvent différer ; nn.MultiheadAttention traite True comme une interdiction pour son masque booléen, alors que certaines fonctions d'attention optimisée utilisent un sens différent. Notre code manuel emploie masked_fill avec True pour interdire explicitement.

ÉQUATION — SOURCE LATEX
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases},\qquad A=\operatorname{softmax}(S+M)

LECTURE À VOIX HAUTE
« M indice i j vaut zéro si j est inférieur ou égal à i, et moins l’infini si j est strictement supérieur à i. »
« A vaut le softmax de la somme de S et de M, appliqué sur les clés de chaque requête. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `M` | « emme » | Matrice du masque additif, compatible avec la matrice des scores. |
| `M_{ij}` | « emme indice i j » | Valeur du masque pour une requête à la position i et une clé à la position j. |
| `\begin{cases}\cdots\end{cases}` | « défini par cas » | L’accolade indique qu’une valeur différente s’applique selon la condition. |
| `j\le i` | « j inférieur ou égal à i » | La clé est à la position courante ou dans le passé ; elle est autorisée. |
| `j>i` | « j strictement supérieur à i » | La clé est dans le futur ; elle est interdite. |
| `0` | « zéro » | Ajouter zéro conserve le score d’une position autorisée. |
| `-\infty` | « moins l’infini » | Valeur idéale qui annule le poids de la position après exponentiation et softmax. |
| `S+M` | « S plus M » | Addition composante par composante des scores et du masque. |
| `A=\operatorname{softmax}(S+M)` | « A égale softmax de S plus M » | Normalisation des seuls scores autorisés ; le softmax opère ligne par ligne. |

INTERPRÉTATION
Pour prédire le prochain token, une position ne doit pas exploiter les tokens suivants. Le masque causal conserve le passé et la position courante. Un masque de padding exclut, lui, les positions de remplissage.

POINT D’ATTENTION
Le zéro signifie ici « autorisé », car il s’agit d’un masque additif. Les conventions des masques booléens dépendent de l’API. Une ligne entièrement masquée nécessite un traitement explicite : le softmax de valeurs toutes égales à −∞ peut produire des NaN.

QUESTION À POSER
Multiplier les scores interdits par zéro suffit-il ?

RÉPONSE ATTENDUE
Non : exp(0) reste positif. Il faut les exclure avant la normalisation.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — MultiheadAttention
https://docs.pytorch.org/docs/2.8/generated/torch.nn.MultiheadAttention.html

## 99. MULTI-HEAD ATTENTION

DIAPOSITIVE 99 — MULTI-HEAD ATTENTION

EXPLICATION TECHNIQUE
Dans la configuration standard, d est divisible par h et chaque tête utilise d_k=d_v=d/h. La concaténation restaure d composantes, puis W_O mélange l'information provenant des têtes. Les têtes peuvent apprendre des relations différentes, mais elles peuvent aussi être redondantes ; on ne doit pas leur attribuer automatiquement une fonction linguistique précise. À largeur d constante, augmenter h n'augmente pas forcément les paramètres des grandes projections, mais modifie la dimension par tête et certains coûts intermédiaires. L'entraînement ajuste ensemble toutes les projections.

ÉQUATION — SOURCE LATEX
\operatorname{head}_r=\operatorname{Attn}(XW_Q^{(r)},XW_K^{(r)},XW_V^{(r)})\\\operatorname{MHA}(X)=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W_O

LECTURE À VOIX HAUTE
« La tête r est obtenue en appliquant l’attention à X fois W Q de la tête r, X fois W K de la tête r, et X fois W V de la tête r. »
« L’attention multi-têtes de X vaut la concaténation des têtes de un à h, multipliée par W indice O. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\operatorname{head}_r` | « tête r » | Sortie de la r-ième tête d’attention. |
| `r,\ h` | « erre ; ache » | r est l’indice d’une tête ; h est le nombre total de têtes. |
| `\operatorname{Attn}` | « attention » | Opération qui calcule les poids à partir des requêtes et clés, puis agrège les valeurs. |
| `W_Q^{(r)},\ W_K^{(r)},\ W_V^{(r)}` | « W Q, W K et W V de la tête r » | Paramètres propres à une tête. Le (r) en haut est une étiquette, pas une puissance. |
| `X` | « iks » | Matrice des représentations d’entrée, de taille n × d. |
| `\operatorname{MHA}(X)` | « attention multi-têtes de X » | MHA signifie Multi-Head Attention. |
| `\operatorname{Concat}` | « concaténation » | Juxtaposition des sorties sur l’axe des caractéristiques, pas addition des têtes. |
| `\ldots` | « jusqu’à » | Les points de suspension représentent toutes les têtes intermédiaires. |
| `W_O` | « W indice O » | Projection finale apprise de taille h d_v × d lorsque chaque tête produit d_v caractéristiques. |

INTERPRÉTATION
Les têtes calculent des agrégations dans plusieurs espaces appris. La concaténation rassemble leurs résultats, puis W_O les recombine dans la dimension attendue par le bloc.

POINT D’ATTENTION
Des têtes distinctes peuvent apprendre des comportements différents, mais leur spécialisation linguistique ou visuelle n’est pas garantie. Si d_v = d/h, la concaténation a exactement d caractéristiques.

QUESTION À POSER
Pour d=256 et h=8, quelle largeur par tête ?

RÉPONSE ATTENDUE
32.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 100. DÉPLIAGE DES AXES MULTI-TÊTES

Étape | Forme standard | Exemple B=2,n=4,d=8,h=2
Projection Q/K/V | B × n × d | 2 × 4 × 8
Séparation des têtes | B × h × n × dₕ | 2 × 2 × 4 × 4
Scores | B × h × n × n | 2 × 2 × 4 × 4
Mélange des valeurs | B × h × n × dₕ | 2 × 2 × 4 × 4
Concaténation | B × n × d | 2 × 4 × 8

DIAPOSITIVE 100 — DÉPLIAGE DES AXES MULTI-TÊTES

EXPLICATION TECHNIQUE
Partir du tenseur B×n×d produit par une projection. On le reforme en B×n×h×d_h, puis on transpose les axes pour obtenir B×h×n×d_h. Le produit avec les clés transposées sur les deux derniers axes donne B×h×n×n. Après le mélange des valeurs, on inverse la permutation et on réunit les têtes. En PyTorch, un transpose peut rendre le stockage non contigu ; reshape sait parfois copier, tandis que view peut exiger contiguous. Le point conceptuel reste de ne pas fusionner des axes qui n'ont pas la même signification.

QUESTION À POSER
Pourquoi transpose-t-on avant de calculer les scores ?

RÉPONSE ATTENDUE
Pour que chaque tête calcule indépendamment ses interactions entre positions.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 101. LAYERNORM : NORMALISER CHAQUE TOKEN

DIAPOSITIVE 101 — LAYERNORM : NORMALISER CHAQUE TOKEN

EXPLICATION TECHNIQUE
Dans le Transformer étudié, chaque token est normalisé séparément sur son dernier axe. Les paramètres gamma et beta ont d composantes partagées entre positions. LayerNorm ne mélange donc pas les tokens et ne transmet pas à elle seule d'information entre positions. Elle n'utilise pas les statistiques mobiles de BatchNorm ; ce contraste explique une partie de son intérêt pour des batches et longueurs variables. La normalisation influe sur l'échelle des activations et la dynamique d'optimisation, mais n'est pas un mécanisme de masquage ni une méthode de correction des fuites de cible.

ÉQUATION — SOURCE LATEX
\mu_i=\frac1d\sum_{r=1}^{d}X_{ir},\quad\operatorname{LN}(X_i)=\gamma\odot\frac{X_i-\mu_i}{\sqrt{\sigma_i^2+\varepsilon}}+\beta

LECTURE À VOIX HAUTE
« Mu indice i vaut un sur d fois la somme, pour r de un à d, de X indice i r. »
« La normalisation de couche de X indice i vaut gamma multiplié composante par composante par X i moins mu i, divisé par la racine carrée de sigma i au carré plus epsilon, puis plus bêta. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `i,\ r` | « i ; erre » | i repère un token ; r repère une caractéristique de ce token. |
| `d` | « dé » | Nombre de caractéristiques sur lesquelles on normalise. |
| `X_{ir},\ X_i` | « X indice i r ; X indice i » | X_ir est un nombre ; X_i est le vecteur complet du token i. |
| `\mu_i` | « mu indice i » | Moyenne des d composantes du token i. |
| `\frac1d\sum_{r=1}^d` | « un sur d fois la somme pour r de un à d » | Calcul d’une moyenne arithmétique. |
| `\sigma_i^2` | « sigma indice i au carré » | Variance des caractéristiques du token i : moyenne des (X_ir − μ_i)². |
| `\varepsilon` | « epsilon » | Petite constante positive ajoutée à la variance pour stabiliser la division. |
| `\sqrt{\sigma_i^2+\varepsilon}` | « racine carrée de sigma i au carré plus epsilon » | Dénominateur complet ; epsilon est sous la racine. |
| `\gamma,\ \beta` | « gamma ; bêta » | Vecteurs appris de taille d : échelle et décalage, partagés entre positions. |
| `\odot` | « multiplié composante par composante » | Produit de Hadamard, à distinguer du produit matriciel. |
| `\operatorname{LN}` | « layer norm » ou « normalisation de couche » | Normalisation ici sur les caractéristiques d’un token, indépendamment des autres tokens. |

INTERPRÉTATION
La moyenne et la variance sont recalculées pour chaque token. On centre et réduit son vecteur, puis on applique une transformation affine apprise. Les scalaires μ_i et σ_i sont diffusés sur les d composantes.

POINT D’ATTENTION
Cette formule ne moyenne pas sur le batch et n’utilise pas les moyennes mobiles de BatchNorm. Le symbole β désigne ici un décalage appris ; dans Adam, il désigne un coefficient de moyenne mobile.

QUESTION À POSER
LayerNorm transmet-elle de l’information d’un token au suivant ?

RÉPONSE ATTENDUE
Pas lorsqu’elle ne normalise que les caractéristiques de chaque token.

LECTURES ET RÉFÉRENCES
Ba et al. — Layer Normalization, 2016
https://arxiv.org/abs/1607.06450

## 102. LE MLP POSITION PAR POSITION

DIAPOSITIVE 102 — LE MLP POSITION PAR POSITION

EXPLICATION TECHNIQUE
Le FFN n'est pas une attention supplémentaire. Il applique un MLP identique à chaque token ; l'échange d'information entre positions a lieu dans l'attention. Avec d_ff=4d et en négligeant les biais, les deux matrices du FFN contiennent 8d² paramètres. Les projections Q, K, V et O d'une auto-attention standard contiennent environ 4d² paramètres : le FFN peut donc représenter une part importante du bloc. L'activation du papier original est ReLU ; nos petits modèles utilisent GELU. Cette différence de variante doit être annoncée sans changer l'explication fondamentale.

ÉQUATION — SOURCE LATEX
\operatorname{FFN}(x)=W_2\,\phi(W_1x+b_1)+b_2,\qquad d\rightarrow d_{\rm ff}\rightarrow d

LECTURE À VOIX HAUTE
« Le réseau feed-forward de x vaut W deux fois phi de W un fois x plus b un, puis plus b deux. »
« La dimension passe de d à d indice F F, puis revient à d. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\operatorname{FFN}` | « feed-forward network » ou « réseau à propagation avant » | Sous-réseau appliqué séparément à chaque position du Transformer. |
| `x` | « iks » | Vecteur colonne d’un token, de dimension d dans cette convention. |
| `W_1,\ W_2` | « W un ; W deux » | Matrices apprises de tailles d_ff × d et d × d_ff. |
| `b_1,\ b_2` | « bé un ; bé deux » | Vecteurs de biais, de dimensions d_ff et d. |
| `\phi` | « phi » | Fonction d’activation non linéaire, appliquée composante par composante, par exemple GELU. |
| `W_1x+b_1` | « W un fois x plus b un » | Première transformation affine, qui produit d_ff caractéristiques. |
| `W_2\phi(W_1x+b_1)+b_2` | « W deux fois phi de W un x plus b un, puis plus b deux » | Deuxième transformation affine après activation. |
| `d,\ d_{\rm ff}` | « dé ; d indice F F » | Dimensions de représentation et de la couche interne du FFN. |
| `\rightarrow` | « passe à » | Flèche indiquant une succession de dimensions, pas une limite mathématique. |

INTERPRÉTATION
L’attention mélange les informations entre positions ; le FFN transforme ensuite les caractéristiques de chaque position. Le même FFN, avec les mêmes poids, s’applique à tous les tokens.

POINT D’ATTENTION
La convention de vecteur colonne explique l’ordre W x ; d’autres slides emploient des tokens en lignes et écrivent X W. Ces écritures sont compatibles en transposant les matrices de paramètres.

QUESTION À POSER
Quelle partie du bloc mélange directement les positions ?

RÉPONSE ATTENDUE
L’attention ; le FFN mélange les caractéristiques de chaque position.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 103. UN BLOC TRANSFORMER PRE-LN

DIAPOSITIVE 103 — UN BLOC TRANSFORMER PRE-LN

EXPLICATION TECHNIQUE
Le papier de 2017 emploie une organisation post-normalisation : normaliser après l'addition résiduelle. Cette diapositive décrit explicitement la variante pre-LN utilisée dans le mini-modèle. Elle modifie la circulation du gradient et les conditions d'optimisation. On ne doit pas présenter une variante comme la seule définition possible d'un Transformer. Les dropout éventuels sont omis de la formule pour faire ressortir les branches ; dans le code, leur place et leur taux doivent être identifiables. Les formes des deux termes additionnés doivent toujours correspondre, y compris lors de changements de largeur.

ÉQUATION — SOURCE LATEX
U=X+\operatorname{MHA}(\operatorname{LN}_1(X))\\Y=U+\operatorname{FFN}(\operatorname{LN}_2(U))

LECTURE À VOIX HAUTE
« U vaut X plus l’attention multi-têtes appliquée à la première normalisation de couche de X. »
« Y vaut U plus le réseau feed-forward appliqué à la deuxième normalisation de couche de U. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X` | « iks » | Entrée du bloc, de taille B × n × d lorsque l’on explicite le batch. |
| `U` | « u » | Représentation intermédiaire après l’attention et la première addition résiduelle. |
| `Y` | « i grec » | Sortie du bloc, après le FFN et la deuxième addition résiduelle. |
| `\operatorname{LN}_1,\ \operatorname{LN}_2` | « normalisation de couche un ; normalisation de couche deux » | Deux normalisations distinctes, avec leurs propres paramètres appris. |
| `\operatorname{MHA}` | « attention multi-têtes » | Sous-couche qui agrège des informations entre positions. |
| `\operatorname{FFN}` | « réseau feed-forward » | Sous-couche qui transforme les caractéristiques de chaque position. |
| `+` | « plus » | Addition composante par composante de la branche transformée et de la branche résiduelle. |
| `\operatorname{MHA}(\operatorname{LN}_1(X))` | « attention de la normalisation de X » | Composition : normaliser d’abord, appliquer l’attention ensuite. |

INTERPRÉTATION
Dans un bloc Pre-LN, la normalisation précède chaque sous-couche. Le chemin résiduel transmet X puis U directement, ce qui facilite la propagation du signal et des gradients.

POINT D’ATTENTION
Les deux termes de chaque addition doivent avoir la même forme. Les flèches de données ne sont pas des mises à jour de poids. Les dropout éventuels sont omis de cette formule.

QUESTION À POSER
Où se place la normalisation dans un bloc post-LN ?

RÉPONSE ATTENDUE
Après la somme entre l’entrée résiduelle et la sortie de la sous-couche.

LECTURES ET RÉFÉRENCES
Xiong et al. — On Layer Normalization in the Transformer Architecture, 2020
https://arxiv.org/abs/2002.04745

## 104. ENCODEUR : CONTEXTUALISER UNE SÉQUENCE

DIAPOSITIVE 104 — ENCODEUR : CONTEXTUALISER UNE SÉQUENCE

EXPLICATION TECHNIQUE
Un encodeur bidirectionnel est utile lorsque toute l'entrée est disponible. Pour une classification de séquence, une représentation spéciale ou une agrégation masquée peut alimenter la tête. Pour une étiquette par token, la tête est appliquée à chaque position. Il faut traiter le padding de manière cohérente dans l'attention, l'agrégation et la perte. L'adjectif bidirectionnel n'implique pas une récurrence : il décrit l'accès aux positions à gauche et à droite. Le même bloc peut être employé avec un masque causal dans une implémentation, mais le régime d'information change alors.

ÉQUATION — SOURCE LATEX
X_L=\operatorname{Block}_L\circ\cdots\circ\operatorname{Block}_1(X_0)

LECTURE À VOIX HAUTE
« X indice L est obtenu en appliquant à X indice zéro le bloc un, puis les blocs suivants, jusqu’au bloc L. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X_0` | « X indice zéro » | Représentations initiales des tokens, après incorporation de l’information de position. |
| `X_L` | « X indice L » | Représentations contextualisées après les L blocs. |
| `L` | « elle majuscule » | Nombre total de blocs de l’encodeur ; à distinguer de la fonction de perte ℒ. |
| `\operatorname{Block}_1,\ \operatorname{Block}_L` | « bloc un ; bloc L » | Premier et dernier blocs du réseau. |
| `\circ` | « composé avec » | Composition de fonctions : la fonction à droite s’applique en premier. |
| `\cdots` | « et ainsi de suite » | Les blocs intermédiaires, de 2 à L − 1. |
| `\operatorname{Block}_L\circ\cdots\circ\operatorname{Block}_1` | « bloc L composé avec les blocs précédents jusqu’au bloc un » | Notation compacte de l’empilement, qui se calcule de droite à gauche. |

INTERPRÉTATION
Chaque bloc reçoit les représentations calculées par le précédent. La succession affine leur contextualisation sans nécessairement changer le nombre de tokens ni leur dimension.

POINT D’ATTENTION
L’ordre de lecture écrit de la composition peut tromper : Block_1 agit en premier. Les blocs ont en général des paramètres distincts, même lorsqu’ils ont la même architecture.

QUESTION À POSER
Peut-on utiliser un encodeur non masqué pour prédire le prochain token sans fuite ?

RÉPONSE ATTENDUE
Non si les tokens futurs sont présents dans son entrée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 105. CROSS-ATTENTION : RELIER DEUX SÉQUENCES

DIAPOSITIVE 105 — CROSS-ATTENTION : RELIER DEUX SÉQUENCES

EXPLICATION TECHNIQUE
Dans un Transformer encodeur-décodeur de traduction, l'encodeur produit une mémoire source contextualisée et le décodeur interroge cette mémoire. Les scores ont alors n cible lignes et n source colonnes. Le masque de padding source interdit les positions ajoutées, tandis que la causalité s'applique principalement à l'auto-attention de la cible. Une cross-attention n'est pas intrinsèquement une traduction : elle peut aussi relier des modalités différentes. Il faut indiquer quels tenseurs fournissent Q et lesquels fournissent K et V pour rendre l'architecture compréhensible.

ÉQUATION — SOURCE LATEX
Q=X_{\rm cible}W_Q,\quad K=H_{\rm source}W_K,\quad V=H_{\rm source}W_V

LECTURE À VOIX HAUTE
« Q vaut X cible fois W Q ; K vaut H source fois W K ; V vaut H source fois W V. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `X_{\rm cible}` | « X cible » | Représentations de la séquence cible qui formule les requêtes. |
| `H_{\rm source}` | « ache source » | Représentations de la séquence source, par exemple produites par un encodeur. |
| `Q` | « ku » | Requêtes calculées à partir de la cible. |
| `K,\ V` | « ka ; vé » | Clés et valeurs calculées à partir de la source. |
| `W_Q,\ W_K,\ W_V` | « W Q ; W K ; W V » | Projections apprises, de tailles adaptées aux dimensions d’entrée et de sortie. |
| `X_{\rm cible}W_Q` | « X cible fois W Q » | Produit matriciel qui conserve le nombre de positions cibles. |
| `H_{\rm source}W_K` | « H source fois W K » | Produit matriciel qui conserve le nombre de positions sources. |
| `{}_{\rm cible},\ {}_{\rm source}` | « indice cible ; indice source » | Étiquettes qui indiquent l’origine des représentations, pas des variables à multiplier. |

INTERPRÉTATION
Chaque position cible interroge les représentations sources. Les poids ont une ligne par position cible et une colonne par position source ; la sortie conserve le nombre de positions cibles.

POINT D’ATTENTION
Le nombre de requêtes peut être différent du nombre de clés. Les dimensions projetées de Q et K doivent coïncider pour calculer les scores ; les dimensions initiales des séquences source et cible ne sont pas nécessairement identiques.

QUESTION À POSER
Quelle longueur retrouve-t-on en sortie de cross-attention ?

RÉPONSE ATTENDUE
La longueur des requêtes, donc celle de la cible ici.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 106. TROIS FAMILLES D’ARCHITECTURES

Famille | Accès aux positions | Exemple de tâche
Encodeur | Toutes les positions disponibles | Classification / étiquetage
Décodeur seul | Passé et position courante | Prédiction du prochain token
Encodeur-décodeur | Source complète + cible causale | Transformation d’une séquence en une autre

DIAPOSITIVE 106 — TROIS FAMILLES D’ARCHITECTURES

EXPLICATION TECHNIQUE
Le nom Transformer couvre plusieurs régimes de calcul. Un encodeur consulte l'entrée disponible dans les deux directions. Un décodeur seul utilise une attention causale pour modéliser une séquence auto-régressive. Un encodeur-décodeur combine une mémoire source et une génération cible avec cross-attention. Le code PyTorch d'un petit décodeur seul peut réutiliser une pile nommée TransformerEncoder avec un masque causal ; le nom de la classe ne détermine pas à lui seul le régime probabiliste. Demander de tracer l'accès à l'information plutôt que de se fier seulement aux noms des composants.

QUESTION À POSER
Un décodeur seul nécessite-t-il une cross-attention ?

RÉPONSE ATTENDUE
Non : il peut ne contenir que de l’auto-attention causale et des FFN.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 107. COÛT DE L’ATTENTION DENSE

DIAPOSITIVE 107 — COÛT DE L’ATTENTION DENSE

EXPLICATION TECHNIQUE
La matrice n×n apparaît pour chaque tête et chaque exemple lorsque l'implémentation la matérialise. Pour n=2048 et h=8, on obtient 33554432 éléments par exemple ; en float32, les seuls scores représentent 128 MiB, avant les gradients et les autres activations. Ce calcul ne constitue pas la mémoire totale d'un modèle. Des algorithmes optimisés évitent de conserver toute la matrice en mémoire tout en calculant l'attention exacte. Ils ne rendent pas automatiquement les interactions denses linéaires en calcul. Le FFN peut dominer pour certaines dimensions et longueurs.

ÉQUATION — SOURCE LATEX
T_{\rm attn}=O(n^2d),\quad T_{\rm proj+FFN}=O(nd^2)\\M_{\rm scores}=O(Bhn^2)\quad\text{si les scores sont materialises}

LECTURE À VOIX HAUTE
« Le coût de l’attention est en grand O de n au carré fois d ; le coût des projections et du FFN est en grand O de n fois d au carré. »
« La mémoire des scores est en grand O de B fois h fois n au carré, si les scores sont matérialisés. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `T_{\rm attn}` | « té indice attention » | Ordre de grandeur du nombre d’opérations pour l’attention dense d’un bloc, par exemple. |
| `T_{\rm proj+FFN}` | « té indice projections et FFN » | Ordre de grandeur du calcul des projections et du réseau feed-forward. |
| `O(\cdot)` | « grand O de » | Notation asymptotique qui décrit une croissance en négligeant des constantes ; ce n’est pas une égalité de temps mesurés. |
| `n` | « enne » | Longueur de la séquence en self-attention. |
| `d` | « dé » | Dimension totale des représentations, répartie entre les têtes. |
| `n^2d` | « n au carré fois d » | Coût des interactions entre toutes les paires de positions. |
| `nd^2` | « n fois d au carré » | Coût des transformations des caractéristiques, si d_ff est proportionnel à d. |
| `M_{\rm scores}` | « emme indice scores » | Nombre d’éléments des matrices de scores stockées. |
| `B,\ h` | « bé majuscule ; ache » | Taille du batch et nombre de têtes. |
| `Bhn^2` | « B fois h fois n au carré » | Une matrice n × n pour chaque tête de chaque exemple. |

INTERPRÉTATION
Doubler la longueur multiplie par quatre le terme quadratique de l’attention, mais seulement par deux les termes linéaires en n. Cela explique les contraintes des longues séquences.

POINT D’ATTENTION
La formule de calcul omet le facteur B et se lit par exemple. La formule mémoire compte des éléments : multiplier par le nombre d’octets par élément pour obtenir des octets. Les implémentations comme FlashAttention évitent de stocker toute la matrice des scores, sans supprimer le nombre quadratique d’interactions de l’attention dense.

QUESTION À POSER
Doubler n multiplie-t-il la taille de la matrice de scores par deux ?

RÉPONSE ATTENDUE
Non : par quatre, à batch et nombre de têtes constants.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 108. ATTENTION MANUELLE : LE CŒUR DU CODE

DIAPOSITIVE 108 — ATTENTION MANUELLE : LE CŒUR DU CODE

EXPLICATION TECHNIQUE
Relier ligne par ligne l'extrait aux trois équations de l'attention. La transposition n'inverse que les deux derniers axes de K ; elle ne permute ni le batch ni la tête. Le masque doit être broadcastable vers la forme des scores. masked_fill retire les scores interdits en leur attribuant moins l'infini. Softmax est appliqué au dernier axe. L'extrait omet volontairement les projections et le dropout pour isoler le noyau du calcul ; le notebook complet les encapsule dans une classe multi-têtes et contrôle les dimensions avant l'agrégation.

QUESTION À POSER
Quelle erreur commet-on en utilisant softmax sur l’axe des requêtes ?

RÉPONSE ATTENDUE
On normalise une autre relation que la distribution des clés pour chaque requête.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 109. TP 04 · VÉRIFIER L’ATTENTION

DIAPOSITIVE 109 — TP 04 · VÉRIFIER L’ATTENTION

EXPLICATION TECHNIQUE
Déroulé : 25 minutes de calcul manuel, 45 minutes pour suivre les axes de la classe multi-têtes, 35 minutes de tests de masques, 25 minutes d'analyse des gradients et 20 minutes de restitution. Le test de causalité remplace les tokens futurs tout en gardant le préfixe identique : les sorties du préfixe doivent rester identiques en mode évaluation, avec dropout désactivé. Une carte d'attention peut illustrer une dépendance calculée, mais ne constitue pas une explication causale complète d'une décision. Les corrigés explicitent aussi le cas d'une ligne entièrement masquée.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Les valeurs numériques de référence et un test qui échouerait si le masque causal était retiré.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 110. EXERCICE · UN BLOC À 256 DIMENSIONS

DIAPOSITIVE 110 — EXERCICE · UN BLOC À 256 DIMENSIONS

EXPLICATION TECHNIQUE
La largeur de tête vaut 256/8=32. Les quatre projections d×d contiennent 4×256²=262144 paramètres. Le FFN contient 256×1024 + 1024×256 =524288 paramètres. Le total des matrices de ces sous-couches est 786432. Cette somme n'inclut pas les embeddings, la tête de sortie, les biais ni les paramètres de normalisation. Les paramètres ne dépendent pas de n pour ces matrices, mais la mémoire d'attention et les activations en dépendent. Faire expliquer pourquoi plusieurs têtes ne multiplient pas nécessairement d'autant le nombre total de paramètres lorsque d reste fixe.

QUESTION À POSER
Quelle sous-couche porte ici deux fois plus de poids matriciels ?

RÉPONSE ATTENDUE
Le FFN : 524 288 contre 262 144 pour les projections d’attention.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 111. JOUR 4 · À RETENIR

DIAPOSITIVE 111 — JOUR 4 · À RETENIR

EXPLICATION TECHNIQUE
Faire reconstruire un bloc sans regarder les diapositives : embedding plus position, normalisation, projections, scores masqués, softmax, valeurs, concaténation, projection, résidu, puis FFN et second résidu. Les détails de variante doivent être annoncés, notamment pre-LN et post-LN. Une question utile consiste à retirer un composant fictivement : sans masque causal, une prédiction de token pourrait lire sa cible ; sans information de position, une auto-attention non masquée conserve l'équivalence par permutation. La journée suivante entraînera effectivement un petit modèle causal et reliera vision et séquences avec les patches.

QUESTION À POSER
Quelle vérification relie directement le code à la causalité ?

RÉPONSE ATTENDUE
Modifier le futur et vérifier que les sorties du préfixe restent identiques.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 112. MODÈLES CAUSAUX ET SYNTHÈSE

DIAPOSITIVE 112 — MODÈLES CAUSAUX ET SYNTHÈSE

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 113. JOUR 5 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Modélisation | Objectif causal, génération et perplexité | 75
Vision Transformer | Patches, position et comparaison aux CNN | 60
Protocole | Ablations, limites et préparation du projet | 45
TP 05 | Mini-Transformer causal sur séquences synthétiques | 180
Évaluation | Restitution argumentée et synthèse transversale | 60

DIAPOSITIVE 113 — JOUR 5 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 114. OBJECTIF AUTO-RÉGRESSIF

DIAPOSITIVE 114 — OBJECTIF AUTO-RÉGRESSIF

EXPLICATION TECHNIQUE
La factorisation par la règle de la chaîne est exacte pour toute distribution de séquence ; le choix architectural détermine comment les probabilités conditionnelles sont paramétrées. Le token de début permet de définir le premier contexte. La moyenne doit ignorer les cibles de padding quand elles ne représentent pas une observation. En entraînement, toutes les positions peuvent être calculées en parallèle grâce au masque causal, même si la génération sera séquentielle. Une séquence avec plusieurs documents concaténés exige une décision sur les frontières et l'information autorisée entre documents.

ÉQUATION — SOURCE LATEX
p_\theta(x_{1:T})=\prod_{t=1}^{T}p_\theta(x_t\mid x_{<t})\\\mathcal L=-\frac1T\sum_{t=1}^{T}\log p_\theta(x_t\mid x_{<t})

LECTURE À VOIX HAUTE
« La probabilité, paramétrée par thêta, de la séquence x de un à T est le produit, pour t de un à T, des probabilités de x t sachant tous les tokens qui le précèdent. »
« La perte L calligraphique vaut moins un sur T fois la somme, pour t de un à T, du logarithme de la probabilité de x t sachant ses prédécesseurs. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `p_\theta` | « pé indice thêta » | Distribution de probabilité du modèle dont les paramètres sont θ. |
| `x_{1:T}` | « x de un à T » | Séquence des T tokens considérés. |
| `x_t` | « x indice t » | Token observé à la position t. |
| `x_{<t}` | « x avant t » ou « tokens précédant t » | Préfixe constitué des tokens de positions strictement inférieures à t. |
| `\mid` | « sachant » | Barre de conditionnement probabiliste ; ce n’est ni une division ni une norme. |
| `\prod_{t=1}^T` | « produit pour t allant de un à T » | Multiplication des probabilités conditionnelles de toutes les positions. |
| `\mathcal L` | « L calligraphique » | Perte de log-vraisemblance négative moyenne. |
| `\sum_{t=1}^T` | « somme pour t de un à T » | Addition des contributions des positions. |
| `-\frac1T` | « moins un sur T » | Change le signe et moyenne sur les T positions. |
| `\log` | « logarithme naturel » | Transforme le produit de probabilités en somme de logarithmes. |

INTERPRÉTATION
La règle de chaîne factorise la probabilité d’une séquence. Maximiser les probabilités des tokens attendus revient à minimiser leur log-vraisemblance négative moyenne.

POINT D’ATTENTION
Le premier token est conditionné sur un préfixe vide ou sur un token de début selon la convention. Ici toutes les T positions comptent ; avec du padding, on moyenne seulement sur les positions valides. T désigne une longueur, pas une transposée.

QUESTION À POSER
Pourquoi l’entraînement peut-il être parallèle alors que la génération est séquentielle ?

RÉPONSE ATTENDUE
Les vrais préfixes sont disponibles au train ; à l’inférence les prochains tokens restent à produire.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 115. DÉCALER ENTRÉES ET CIBLES

DIAPOSITIVE 115 — DÉCALER ENTRÉES ET CIBLES

EXPLICATION TECHNIQUE
Montrer une séquence très courte avec des identifiants : [BOS,2,4,EOS]. L'entrée est [BOS,2,4] et la cible [2,4,EOS]. La sortie à la position de 2 doit prédire 4 en ayant accès à BOS et 2, mais pas à 4 en entrée future. Si l'on donne la même séquence comme entrée et cible, le modèle peut apprendre à copier le token qu'il voit déjà. Ce bug peut produire une perte très faible et une génération inutile. Le test de causalité et la lecture du décalage sont donc complémentaires.

ÉQUATION — SOURCE LATEX
\text{inputs}=s_{0:T-1},\qquad\text{targets}=s_{1:T}

LECTURE À VOIX HAUTE
« Les entrées sont les tokens de la séquence s allant de l’indice zéro à l’indice T moins un inclus. Les cibles sont les tokens allant de l’indice un à l’indice T inclus. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `s` | « esse » | Séquence de T + 1 tokens, indexés de zéro à T. |
| `\text{inputs}` | « entrées » | Suite des T tokens fournis au modèle. |
| `\text{targets}` | « cibles » | Suite des T tokens que le modèle doit prédire. |
| `s_{0:T-1}` | « s de zéro à T moins un » | Tokens d’indices 0, 1, …, T − 1, dans la convention inclusive de cette formule. |
| `s_{1:T}` | « s de un à T » | Tokens d’indices 1, 2, …, T, dans la même convention. |
| `:` | « de … à … » | Indique un intervalle d’indices dans cette notation mathématique. |
| `T-1` | « T moins un » | Dernier indice de l’entrée ; la soustraction porte sur l’indice. |
| `T` | « té majuscule » | Nombre de positions prédites et dernier indice de la séquence initiale. |

INTERPRÉTATION
Chaque entrée est associée au token suivant. Pour s = [BOS, a, b, EOS], les entrées sont [BOS, a, b] et les cibles [a, b, EOS]. Le masque causal empêche chaque entrée d’utiliser les tokens suivants.

POINT D’ATTENTION
Les bornes écrites ici sont inclusives. En Python, la borne de fin d’un slice est exclusive : utiliser s[:-1] et s[1:] pour réaliser ce décalage. Copier littéralement s[0:T-1] supprimerait un token de trop.

QUESTION À POSER
Une perte quasi nulle dès le départ peut-elle révéler un mauvais décalage ?

RÉPONSE ATTENDUE
Oui : le modèle peut voir directement le token qu’on lui demande de prédire.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 116. TEACHER FORCING ET GÉNÉRATION

DIAPOSITIVE 116 — TEACHER FORCING ET GÉNÉRATION

EXPLICATION TECHNIQUE
Ce contraste est souvent appelé différence d'exposition aux contextes. La vraisemblance reste un objectif bien défini, mais une bonne performance conditionnée par les vrais préfixes ne garantit pas une génération de longue durée sans dérive. Dans le TP, on évalue séparément la perte sur séquences tenues à part et la capacité de continuation après un préfixe fixé. Les séquences sont synthétiques pour rendre la règle attendue explicite. Les modèles de langage réels ajoutent des contraintes de données, de tokenisation et d'usage qui ne sont pas reproduites par ce petit laboratoire.

QUESTION À POSER
Pourquoi vérifier aussi des continuations libres ?

RÉPONSE ATTENDUE
Pour observer le comportement lorsque le modèle conditionne sur ses propres sorties.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 117. DÉCODAGE : ARGMAX, TEMPÉRATURE ET ÉCHANTILLONNAGE

DIAPOSITIVE 117 — DÉCODAGE : ARGMAX, TEMPÉRATURE ET ÉCHANTILLONNAGE

EXPLICATION TECHNIQUE
Une petite température concentre la masse vers les plus grands logits ; une grande température aplatit la distribution. La limite vers zéro approche une sélection des maxima, mais diviser effectivement par zéro est une erreur. Top-k garde un nombre fixe de candidats ; top-p conserve un ensemble dont la masse cumulée atteint un seuil selon la règle employée. Ces transformations changent la distribution de génération et ne corrigent pas une connaissance erronée. Dans le TP, commencer par un décodage glouton pour comprendre le mécanisme, puis varier la température avec une graine de tirage explicite.

ÉQUATION — SOURCE LATEX
p_\tau(x_t=k\mid x_{<t})=\operatorname{softmax}(z/\tau)_k,\qquad\tau>0

LECTURE À VOIX HAUTE
« La probabilité, à température tau, que le token t soit k sachant le préfixe vaut la composante k du softmax des logits z divisés par tau, avec tau strictement positif. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `p_\tau` | « pé indice tau » | Distribution de génération après réglage de la température. |
| `x_t=k` | « x indice t égal à k » | Événement : choisir le token d’identifiant k à la position t. |
| `x_{<t}` | « tokens précédant t » | Contexte utilisé pour calculer les logits. |
| `\mid` | « sachant » | Conditionnement sur le préfixe. |
| `z` | « zède » | Vecteur des logits, avec une composante par token du vocabulaire. |
| `\tau` | « tau » | Température, un scalaire positif qui règle la concentration de la distribution. |
| `z/\tau` | « z divisé par tau » | Division de chaque logit par le même scalaire avant le softmax. |
| `\operatorname{softmax}(z/\tau)_k` | « composante k du softmax de z sur tau » | Probabilité du token k après normalisation. |
| `\tau>0` | « tau strictement supérieur à zéro » | Condition nécessaire à cette formule. |

INTERPRÉTATION
Une petite température accentue les écarts entre logits et concentre les probabilités. Une grande température les atténue et rend la distribution plus uniforme.

POINT D’ATTENTION
On divise les logits, pas les probabilités déjà normalisées. Tau égal à zéro rend l’écriture indéfinie ; le décodage glouton est un choix séparé, ou une limite quand tau tend vers zéro avec un maximum unique. Une température basse ne garantit pas l’exactitude de la réponse.

QUESTION À POSER
Une température plus faible garantit-elle une réponse correcte ?

RÉPONSE ATTENDUE
Non : elle concentre la distribution du modèle, y compris sur ses erreurs.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 118. PERPLEXITÉ ET NORMALISATION DE LA PERTE

DIAPOSITIVE 118 — PERPLEXITÉ ET NORMALISATION DE LA PERTE

EXPLICATION TECHNIQUE
V désigne ici l'ensemble des positions valides, et non la taille du vocabulaire utilisée précédemment ; le préciser oralement. Pour éviter l'ambiguïté, parler de positions évaluées. Une distribution uniforme sur dix tokens a une perplexité de dix lorsque ces dix tokens sont les cibles possibles. Une perplexité de un correspond à une probabilité un sur les cibles observées dans cette évaluation, limite idéale. La perplexité d'un modèle à caractères et celle d'un modèle à sous-mots n'ont pas la même unité de normalisation. Dans le TP, les premiers symboles aléatoires restent intrinsèquement difficiles à prédire.

ÉQUATION — SOURCE LATEX
\operatorname{PPL}=\exp\!\left(-\frac1M\sum_{t\in\mathcal V}\log p_\theta(x_t\mid x_{<t})\right),\quad M=|\mathcal V|

LECTURE À VOIX HAUTE
« La perplexité vaut l’exponentielle de moins un sur M fois la somme, sur les positions t appartenant à V calligraphique, du logarithme de la probabilité du token x t sachant les tokens précédents. »
« M est égal au cardinal de V calligraphique, c’est-à-dire au nombre de positions valides. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\operatorname{PPL}` | « perplexité » | Exponentielle de la perte moyenne de log-vraisemblance négative. |
| `\exp` | « exponentielle » | Fonction inverse du logarithme naturel. |
| `\mathcal V` | « V calligraphique » | Ensemble des positions valides, après exclusion du padding et des positions ignorées. |
| `t\in\mathcal V` | « t appartient à V calligraphique » | Seules ces positions sont incluses dans la somme. |
| `\sum_{t\in\mathcal V}` | « somme sur les t appartenant à V calligraphique » | Addition des log-probabilités de tous les tokens évalués. |
| `M=\|\mathcal V\|` | « M égale le cardinal de V calligraphique » | M est le nombre de positions valides ; les barres simples désignent ici un cardinal. |
| `p_\theta(x_t\mid x_{<t})` | « probabilité de x t sachant les précédents, sous le modèle thêta » | Probabilité attribuée par le modèle au token réellement observé. |
| `\log` | « logarithme naturel » | Logarithme en base e, cohérent avec l’exponentielle utilisée. |
| `-\frac1M` | « moins un sur M » | Calcule la moyenne négative, en supposant M strictement positif. |

INTERPRÉTATION
La perplexité est une transformation de la perte : une meilleure log-probabilité moyenne donne une perplexité plus faible. Une perte égale à log(8), par exemple, correspond à une perplexité de 8.

POINT D’ATTENTION
V calligraphique représente ici des positions, pas le vocabulaire ni la matrice des valeurs d’attention. Comparer des perplexités exige la même tokenisation et le même protocole d’évaluation. La moyenne se calcule sur tous les tokens valides, sans moyenner naïvement des moyennes de batches de tailles différentes.

QUESTION À POSER
Que vaut exp(log(8)) ?

RÉPONSE ATTENDUE
8 ; c’est la perplexité d’un choix uniforme parmi huit possibilités.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 119. CACHE K/V À L’INFÉRENCE

DIAPOSITIVE 119 — CACHE K/V À L’INFÉRENCE

EXPLICATION TECHNIQUE
Dans une multi-head attention standard, la largeur totale des clés et celle des valeurs valent souvent d, donc d_KV=d. Des variantes à clés et valeurs partagées changent ce facteur. Le cache contient un tenseur K et un tenseur V par couche, batch et position. Pour chaque nouveau token, on ne recalcule pas les projections du passé, mais on doit toujours comparer sa requête aux clés conservées. La mémoire croît donc avec la longueur de contexte. Le mini-modèle du TP recalcule volontairement le préfixe complet pour rester lisible ; il n'implémente pas de cache.

ÉQUATION — SOURCE LATEX
M_{KV}\approx2BLnd_{KV}\times\text{octets par element}

LECTURE À VOIX HAUTE
« La mémoire du cache clés-valeurs vaut approximativement deux fois B fois L fois n fois d indice K V, multiplié par le nombre d’octets par élément. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `M_{KV}` | « emme indice K V » | Mémoire totale du cache de clés et valeurs, exprimée ici en octets. |
| `\approx` | « approximativement égal à » | Estimation qui ignore notamment les surcoûts d’allocation. |
| `2` | « deux » | Deux familles de tenseurs à stocker : les clés et les valeurs. |
| `B` | « bé majuscule » | Nombre de séquences dans le batch. |
| `L` | « elle majuscule » | Nombre de couches dont on conserve le cache. |
| `n` | « enne » | Nombre de positions déjà mises en cache par séquence. |
| `d_{KV}` | « d indice K V » | Largeur totale des clés, ou des valeurs, toutes têtes KV réunies, pour un token et une couche. |
| `\times` | « multiplié par » | Produit des dimensions et de la taille d’un élément. |
| `\text{octets par element}` | « octets par élément » | Taille du type numérique utilisé : par exemple deux octets pour float16. |

INTERPRÉTATION
Le cache évite de recalculer les clés et valeurs des tokens précédents pendant la génération. Son volume croît linéairement avec le batch, le nombre de couches et la longueur mémorisée.

POINT D’ATTENTION
Le facteur deux suppose la même largeur et le même type numérique pour K et V. d_KV inclut déjà toutes les têtes KV : ne pas remultiplier par leur nombre. Cette estimation exclut les poids du modèle et les autres buffers. En attention multi-têtes standard d_KV = d ; le partage des têtes KV peut le réduire.

QUESTION À POSER
Le cache supprime-t-il le besoin de consulter les tokens passés ?

RÉPONSE ATTENDUE
Non : il réutilise leurs clés et valeurs déjà calculées.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 120. VISION TRANSFORMER : UNE IMAGE EN PATCHES

DIAPOSITIVE 120 — VISION TRANSFORMER : UNE IMAGE EN PATCHES

EXPLICATION TECHNIQUE
La formule suppose H et W divisibles par P et des patches carrés de côté P. Chaque patch est converti en vecteur, puis en embedding appris. Un token de classification peut être ajouté ; d'autres variantes utilisent une agrégation des sorties. La couche de projection peut être implémentée comme une convolution de noyau P et de stride P, ce qui relie les deux familles sans les rendre identiques. Les positions sont indispensables pour préserver l'organisation spatiale dans l'approche standard. Une réduction de P augmente fortement le nombre de tokens et le coût de l'attention.

ÉQUATION — SOURCE LATEX
n=\frac{HW}{P^2},\qquad x_i\in\mathbb R^{P^2C},\qquad z_i=x_iW_E+p_i

LECTURE À VOIX HAUTE
« Le nombre de patches n vaut H fois W divisé par P au carré. Chaque patch aplati x indice i appartient à l’espace réel de dimension P au carré fois C. »
« z indice i vaut x indice i fois W indice E, plus p indice i. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `H,\ W` | « ache ; double vé » | Hauteur et largeur de l’image, en pixels. |
| `P` | « pé majuscule » | Longueur du côté d’un patch carré, en pixels. |
| `P^2` | « P au carré » | Nombre de pixels spatiaux d’un patch. |
| `C` | « cé majuscule » | Nombre de canaux, par exemple trois pour une image RGB. |
| `n=HW/P^2` | « n égale H fois W sur P au carré » | Nombre de patches non chevauchants, avant l’ajout éventuel de tokens spéciaux. |
| `x_i\in\mathbb R^{P^2C}` | « x i appartient à l’espace réel de dimension P au carré fois C » | Vecteur des pixels du patch i, après aplatissement. |
| `W_E` | « W indice E » | Matrice de projection apprise de taille (P²C) × d. |
| `p_i` | « pé minuscule indice i » | Vecteur de position associé au patch i, de dimension d. |
| `z_i` | « zède indice i » | Représentation du patch de dimension d, après projection et ajout de position. |
| `x_iW_E` | « x i fois W E » | Produit matriciel écrit avec x_i sous forme de vecteur ligne. |

INTERPRÉTATION
Une image est convertie en séquence de patches. Chaque patch est aplati, projeté dans l’espace du Transformer, puis enrichi de son information de position.

POINT D’ATTENTION
On suppose H et W divisibles par P, avec des patches carrés non chevauchants. P désigne ici une taille de patch, pas un nombre de paramètres. Le p_i minuscule est un vecteur de position, pas une probabilité ; la formule de n exclut un éventuel token CLS.

QUESTION À POSER
Combien de valeurs dans un patch RGB 16×16 ?

RÉPONSE ATTENDUE
16×16×3 = 768.

LECTURES ET RÉFÉRENCES
Dosovitskiy et al. — An Image is Worth 16x16 Words, 2020
https://arxiv.org/abs/2010.11929

## 121. PATCHES : CALCULER LE COÛT

DIAPOSITIVE 121 — PATCHES : CALCULER LE COÛT

EXPLICATION TECHNIQUE
Le dernier rapport porte uniquement sur les matrices d'attention des tokens visuels sans token de classification. En ajoutant ce token, le rapport exact devient 785²/197², légèrement différent de seize. Cette précision montre l'intérêt de distinguer une approximation d'ordre de grandeur d'un calcul exact. La projection de chaque patch change aussi avec P ; tout le coût du modèle ne suit donc pas nécessairement le même facteur. Des patches plus petits gardent une granularité spatiale plus fine, mais le compromis dépend de la tâche, des données et du budget.

ÉQUATION — SOURCE LATEX
\left(\frac{224}{16}\right)^2=196,\qquad\left(\frac{224}{8}\right)^2=784\\\frac{784^2}{196^2}=16

LECTURE À VOIX HAUTE
« Deux cent vingt-quatre divisé par seize, le quotient au carré, vaut cent quatre-vingt-seize. »
« Deux cent vingt-quatre divisé par huit, le quotient au carré, vaut sept cent quatre-vingt-quatre. »
« Sept cent quatre-vingt-quatre au carré divisé par cent quatre-vingt-seize au carré vaut seize. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `224` | « deux cent vingt-quatre » | Hauteur et largeur en pixels de l’image carrée. |
| `16,\ 8` | « seize ; huit » | Deux tailles possibles pour le côté d’un patch carré. |
| `224/16,\ 224/8` | « deux cent vingt-quatre sur seize ; sur huit » | Nombres de patches le long d’un seul côté : 14 et 28. |
| `(224/16)^2` | « le quotient deux cent vingt-quatre sur seize, au carré » | Nombre total de patches de 16 × 16 pixels : 14 × 14 = 196. |
| `(224/8)^2` | « le quotient deux cent vingt-quatre sur huit, au carré » | Nombre total de patches de 8 × 8 pixels : 28 × 28 = 784. |
| `196,\ 784` | « cent quatre-vingt-seize ; sept cent quatre-vingt-quatre » | Longueurs des deux séquences de patches, sans token spécial. |
| `784^2/196^2` | « sept cent quatre-vingt-quatre au carré sur cent quatre-vingt-seize au carré » | Rapport des nombres de paires de patches dans l’attention dense. |
| `16` | « seize » | Facteur de croissance du nombre de scores d’attention lorsque la taille du patch est divisée par deux. |

INTERPRÉTATION
Diviser par deux le côté des patches multiplie par quatre leur nombre. Comme chaque patch peut interagir avec tous les autres, le nombre de paires est alors multiplié par seize.

POINT D’ATTENTION
Le carré dans la première ligne compte les deux axes de l’image ; le carré dans la deuxième ligne compte les paires de tokens. Le facteur seize concerne les scores et le terme quadratique de l’attention, pas nécessairement le temps total du modèle ni toutes ses allocations mémoire.

QUESTION À POSER
Diviser la taille de patch par deux double-t-il n ?

RÉPONSE ATTENDUE
Non : n est multiplié par quatre pour une image 2D.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 122. CNN ET VIT : COMPARER LES HYPOTHÈSES

Aspect | CNN standard | ViT standard
Interaction initiale | Locale, noyaux partagés | Patches puis attention globale
Position | Structure de grille dans les opérations | Encodage explicite des positions
Résolution | Champ réceptif progressif | Nombre de patches / tokens
Coût typique | Dépend des cartes et des noyaux | Attention dense quadratique en tokens
Conclusion | À valider pour la tâche | À valider pour la tâche

DIAPOSITIVE 122 — CNN ET VIT : COMPARER LES HYPOTHÈSES

EXPLICATION TECHNIQUE
Éviter un classement absolu des architectures. Les CNN imposent une localité et un partage spatiaux forts ; les Transformers permettent un mélange global dépendant du contenu dans les couches d'attention denses. Les données, le préentraînement, les augmentations, la résolution et le budget peuvent modifier les conclusions empiriques. Un ViT ne devient pas automatiquement supérieur parce qu'il appartient à une famille plus récente. Les architectures hybrides et hiérarchiques rendent la frontière moins stricte. L'évaluation doit comparer des recettes documentées plutôt qu'un nom de famille isolé.

QUESTION À POSER
Quel contrôle est indispensable pour comparer CNN et ViT ?

RÉPONSE ATTENDUE
Le protocole de données, préentraînement, résolution et budget de calcul.

LECTURES ET RÉFÉRENCES
Dosovitskiy et al. — An Image is Worth 16x16 Words, 2020
https://arxiv.org/abs/2010.11929

## 123. TRANSFERT DANS UN TRANSFORMER

DIAPOSITIVE 123 — TRANSFERT DANS UN TRANSFORMER

EXPLICATION TECHNIQUE
Le même principe backbone-tête vu pour les CNN s'applique aux encodeurs Transformers, mais avec des choix supplémentaires : tokenisation, positions, masque et agrégation. Pour un modèle causal, la tâche peut être formulée comme une prédiction de séquence ; il faut vérifier que les cibles et le masquage de perte correspondent à l'objectif. Les méthodes d'adaptation à faible nombre de paramètres sont une extension possible, pas détaillée dans ce cours d'introduction. Un petit nombre de paramètres adaptés ne garantit ni un faible coût d'inférence ni une absence d'oubli sur la tâche source.

QUESTION À POSER
Changer seulement la tête suffit-il si la tokenisation est incompatible ?

RÉPONSE ATTENDUE
Non : les identifiants, embeddings et prétraitements doivent rester cohérents.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 124. LIMITES ET INTERPRÉTATION

DIAPOSITIVE 124 — LIMITES ET INTERPRÉTATION

EXPLICATION TECHNIQUE
Les informations peuvent transiter par plusieurs têtes, les valeurs, les résidus et les MLP ; une carte d'attention ne décrit donc qu'une partie du calcul. Une vérification causale demanderait des interventions contrôlées, elles-mêmes à interpréter prudemment. Pour les modèles génératifs, la vraisemblance entraîne la prédiction de séquences, pas une garantie de vérité. Dans un projet appliqué, analyser les populations concernées, la provenance et l'autorisation d'usage des données, ainsi que les risques d'erreurs spécifiques au domaine. Les exemples jouets du cours ne valident pas ces conditions de déploiement.

QUESTION À POSER
Une carte d’attention suffit-elle à prouver pourquoi une classe a été prédite ?

RÉPONSE ATTENDUE
Non : elle ne couvre qu’une partie des chemins de calcul.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 125. TP 05 : LA TÂCHE ET SON PROTOCOLE

DIAPOSITIVE 125 — TP 05 : LA TÂCHE ET SON PROTOCOLE

EXPLICATION TECHNIQUE
Les quatre premiers symboles sont choisis dans un alphabet de huit possibilités. Ils ne peuvent pas tous être déduits du préfixe ; une partie de la perte est donc irréductible pour cette distribution. Les répétitions suivantes constituent les positions de copie prévisibles. Le découpage se fait sur les motifs de quatre symboles, avant la répétition, pour éviter qu'une séquence identique soit présente dans plusieurs partitions. Il s'agit d'une tâche synthétique de structure séquentielle, pas d'une évaluation linguistique. La métrique de copie complète la perplexité et permet de distinguer apprentissage de la règle et prédiction des symboles initiaux.

ÉQUATION — SOURCE LATEX
\langle BOS\rangle,\ a,b,c,d,\ a,b,c,d,\ a,b,c,d,\ \langle EOS\rangle

LECTURE À VOIX HAUTE
« Token de début de séquence, puis a, b, c, d ; à nouveau a, b, c, d ; une troisième fois a, b, c, d ; puis token de fin de séquence. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\langle BOS\rangle` | « token de début de séquence » | BOS signifie Begin Of Sequence. C’est un symbole spécial du vocabulaire. |
| `\langle EOS\rangle` | « token de fin de séquence » | EOS signifie End Of Sequence. Le modèle apprend notamment à prédire ce symbole. |
| `a,\ b,\ c,\ d` | « a ; bé ; cé ; dé » | Quatre tokens du motif à répéter ; ces lettres ne désignent ici ni des dimensions ni des paramètres. |
| `\langle\ \rangle` | « chevrons » | Délimitent le nom d’un token spécial ; ils ne représentent pas un produit scalaire. |
| `,` | « puis » | Sépare les positions successives dans cette représentation de la séquence. |
| `a,b,c,d\;\text{repete trois fois}` | « le motif a, b, c, d répété trois fois » | Dépendance synthétique que le modèle doit apprendre à reproduire. |

INTERPRÉTATION
Cette tâche artificielle rend visibles les dépendances entre tokens : le modèle doit retrouver le motif, le répéter et s’arrêter. L’exemple comporte 14 tokens si l’on compte BOS et EOS.

POINT D’ATTENTION
L’exemple illustre la structure du jeu de données du TP, pas une équation algébrique. Prédire une répétition sur ce jeu ne démontre pas une compréhension générale du langage. L’entraînement doit toujours décaler les cibles d’un token.

QUESTION À POSER
Pourquoi ne pas exiger une perte globale nulle ?

RÉPONSE ATTENDUE
Les symboles initiaux du motif sont aléatoires et ne sont pas entièrement prévisibles.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 126. TP 05 · ENTRAÎNER UN MINI-TRANSFORMER

DIAPOSITIVE 126 — TP 05 · ENTRAÎNER UN MINI-TRANSFORMER

EXPLICATION TECHNIQUE
Organisation : 25 minutes pour les données et l'objectif, 40 minutes d'inspection du bloc et des masques, 40 minutes d'entraînement et d'évaluation, 40 minutes d'ablation et 35 minutes de restitution. Les étudiants doivent d'abord prouver l'absence d'accès au futur. Le test modifie la fin d'une entrée et vérifie les logits du préfixe. L'ablation choisit un facteur, par exemple la position ou le nombre de têtes, puis reconduit le même protocole. Un modèle qui apprend imparfaitement la copie reste utile pour étudier le diagnostic. Le notebook inclut aussi un exercice de mise en patches sans entraînement d'un grand ViT.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Une expérience reproductible et une explication des mécanismes, même si la copie reste imparfaite.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 127. ABLATIONS : CHANGER UN FACTEUR

Modification | Hypothèse à tester | Contrôle requis
Sans position | Effet de l’information d’ordre | Même données et budget
Une seule tête | Diversité des projections | Largeur totale fixée
Plus de couches | Capacité / optimisation | Coût et normes des gradients
Sans masque causal | Détection de fuite | Test de préfixe doit échouer

DIAPOSITIVE 127 — ABLATIONS : CHANGER UN FACTEUR

EXPLICATION TECHNIQUE
Faire annoncer l'hypothèse avant l'exécution. Une ablation utile doit préciser ce qui reste fixé et ce qui change. Retirer le masque causal est un contrôle de fuite, pas une amélioration admissible de l'objectif auto-régressif. Retirer les positions teste un mécanisme différent et peut ne pas dégrader toutes les tâches de la même manière. Modifier les têtes à largeur fixe ne modifie pas nécessairement les paramètres comme le ferait une modification de d. Les conclusions doivent citer le nombre de graines et le budget réellement exécuté, et distinguer une observation locale d'une propriété générale.

QUESTION À POSER
Si un modèle sans masque obtient une meilleure perte, peut-on le déclarer meilleur en génération causale ?

RÉPONSE ATTENDUE
Non : il peut exploiter les tokens futurs et résoudre un autre problème.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 128. ÉVALUATION FINALE : EXPLIQUER ET PROUVER

Critère | Preuve | Points
Compréhension mathématique | Dérivation et dimensions | 5
Implémentation | Calcul vérifié et masques corrects | 5
Protocole expérimental | Séparation et sélection sans fuite | 5
Analyse et limites | Erreurs, ablation et discussion | 5

DIAPOSITIVE 128 — ÉVALUATION FINALE : EXPLIQUER ET PROUVER

EXPLICATION TECHNIQUE
Le barème proposé totalise vingt points et peut être adapté au règlement de la formation. Évaluer une présentation de dix minutes par binôme, accompagnée d'un notebook exécuté et d'un court compte rendu individuel. Faire poser une question de gradient, une question de formes et une question de validité expérimentale. Ne pas attribuer tous les points à l'accuracy : un résultat performant avec fuite de données échoue sur le protocole. Inversement, un résultat limité mais bien contrôlé peut démontrer la maîtrise des mécanismes et une capacité de diagnostic.

QUESTION À POSER
Quelle preuve doit accompagner un score ?

RÉPONSE ATTENDUE
Le protocole qui permet de comprendre ce que ce score estime.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 129. SYNTHÈSE : UN MÊME CADRE, PLUSIEURS STRUCTURES

DIAPOSITIVE 129 — SYNTHÈSE : UN MÊME CADRE, PLUSIEURS STRUCTURES

EXPLICATION TECHNIQUE
Revenir à l'unité conceptuelle du cours. Un MLP, un CNN et un Transformer diffèrent par leurs opérations et les contraintes qu'ils imposent, mais chacun définit une fonction paramétrée et une perte différentiable. La rétropropagation traverse le graphe correspondant ; l'optimiseur utilise ses gradients. Les paramètres de convolution sont partagés entre positions spatiales, ceux du FFN Transformer entre tokens, et les poids d'attention eux-mêmes sont calculés à partir du contenu. La performance dépend ensuite des données et de l'évaluation, pas uniquement de la famille du modèle.

ÉQUATION — SOURCE LATEX
\text{donnees}\ \longrightarrow\ f_\theta\ \longrightarrow\ \mathcal L\ \xrightarrow{\rm backprop}\ \nabla_\theta\mathcal L\ \xrightarrow{\rm optimiseur}\ \theta'

LECTURE À VOIX HAUTE
« Les données passent dans le modèle paramétré par thêta ; les prédictions permettent de calculer la perte L calligraphique ; la rétropropagation calcule son gradient par rapport à thêta ; l’optimiseur utilise ce gradient pour obtenir les paramètres mis à jour, thêta prime. »

SYMBOLES : NOM À PRONONCER ET SENS

| Symbole | Nom à prononcer | Sens ici |
| --- | --- | --- |
| `\text{donnees}` | « données » | Entrées du modèle ; les cibles participent aussi au calcul de la perte supervisée même si elles ne sont pas dessinées ici. |
| `f_\theta` | « effe indice thêta » | Fonction représentée par le réseau, avec ses paramètres θ. |
| `\mathcal L` | « L calligraphique » | Objectif scalaire calculé à partir des prédictions et des cibles dans le cadre supervisé. |
| `\nabla` | « nabla » | Symbole qui désigne un gradient. |
| `\nabla_\theta\mathcal L` | « gradient de L par rapport à thêta » | Ensemble des dérivées partielles de la perte par rapport à chacun des paramètres. |
| `\xrightarrow{\rm backprop}` | « puis, par rétropropagation » | Étape qui applique la règle de la chaîne pour calculer les dérivées. |
| `\xrightarrow{\rm optimiseur}` | « puis, par l’optimiseur » | Étape qui détermine la mise à jour à partir du gradient et, selon l’algorithme, de son état interne. |
| `\theta'` | « thêta prime » | Nouvelles valeurs des paramètres après une étape ; le prime n’est pas ici une dérivée. |
| `\longrightarrow` | « conduit à » ou « passe dans » | Flèche de déroulement du calcul ; elle n’exprime pas une égalité. |

INTERPRÉTATION
Ce schéma rassemble la boucle d’apprentissage : prédire, mesurer l’erreur, calculer les dérivées et mettre à jour les paramètres. Les nouvelles valeurs servent au passage suivant.

POINT D’ATTENTION
La rétropropagation calcule des gradients ; elle ne choisit pas à elle seule la mise à jour. C’est l’optimiseur qui effectue cette mise à jour. Le gradient n’est ni une probabilité ni une nouvelle prédiction.

QUESTION À POSER
Qu’est-ce qui change entre MLP, CNN et Transformer ?

RÉPONSE ATTENDUE
Le graphe de calcul et ses hypothèses de structure, tout en gardant le cadre d’apprentissage.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 130. EXERCICE DE SYNTHÈSE : AUDIT D’UN MODÈLE

DIAPOSITIVE 130 — EXERCICE DE SYNTHÈSE : AUDIT D’UN MODÈLE

EXPLICATION TECHNIQUE
Corrigé : les cibles doivent être décalées d'un token par rapport aux entrées. Sinon, la position courante voit déjà le symbole à prédire. Un masque additif constitué de zéros et de uns n'interdit aucune position ; il décale seulement les scores. Le masque doit utiliser moins l'infini pour les positions interdites, ou une convention booléenne correctement interprétée par l'API. Tester un petit exemple explicite de décalage et modifier les tokens futurs tout en comparant les logits du préfixe en mode évaluation. Vérifier également les sommes des poids et les entrées de la matrice masquée.

QUESTION À POSER
Quels deux contrôles doit-on exécuter avant de relancer l’entraînement ?

RÉPONSE ATTENDUE
Un exemple entrée/cible décalé et un test d’invariance du préfixe aux modifications du futur.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 131. LECTURES FOURNIES : FONDEMENTS ET MÉTHODE

DIAPOSITIVE 131 — LECTURES FOURNIES : FONDEMENTS ET MÉTHODE

EXPLICATION TECHNIQUE
Ces quatre supports constituent des lectures complémentaires, pas des textes à mémoriser intégralement. Bigot fournit une entrée mathématique sur le risque, les réseaux multicouches et les CNN. Le cours de Tavenard, dans sa version PDF datée du 11 août 2025, couvre aussi la régularisation, les architectures et l'attention. Le support RCP 209 2025–2026 du CNAM est signé Javiera Castillo Navarro. Geoffrey Daniel insiste sur l'utilisation et la méthodologie. La version HTML de Tavenard permet une navigation par chapitre. Les numéros indiqués ci-dessous sont ceux des pages PDF lorsqu'ils sont cités dans le guide.

QUESTION À POSER
Quelle lecture reprendre pour revoir les notions de risque et de réseau multicouche ?

RÉPONSE ATTENDUE
Le support de Jérémie Bigot et les chapitres 1 à 4 de Tavenard.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

Geoffrey Daniel — Réseaux de neurones et deep learning : utilisation et méthodologie
https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf

Romain Tavenard — Version HTML du cours
https://rtavenar.github.io/deep_book/fr/content/fr/intro.html

## 132. ARTICLES : ARCHITECTURES ET OPTIMISATION

DIAPOSITIVE 132 — ARTICLES : ARCHITECTURES ET OPTIMISATION

EXPLICATION TECHNIQUE
Utiliser les articles pour distinguer la définition historique d'une architecture des variantes modernes. Attention Is All You Need décrit un Transformer encodeur-décodeur avec post-normalisation. ResNet introduit la formulation résiduelle pour la vision. Le travail sur ViT montre comment traiter une image comme une séquence de patches dans un régime de préentraînement explicite. Adam et AdamW répondent à des choix d'optimisation différents. Lire les sections de méthode avant les tableaux de scores, puis demander quelles données, quel budget et quelle évaluation rendent ces scores interprétables.

QUESTION À POSER
Pourquoi revenir à l’article original ?

RÉPONSE ATTENDUE
Pour identifier les hypothèses et les choix exacts de l’architecture étudiée.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

He et al. — Deep Residual Learning for Image Recognition, 2015
https://arxiv.org/abs/1512.03385

Dosovitskiy et al. — An Image is Worth 16x16 Words, 2020
https://arxiv.org/abs/2010.11929

Kingma et Ba — Adam, 2014
https://arxiv.org/abs/1412.6980

Loshchilov et Hutter — Decoupled Weight Decay Regularization, 2017
https://arxiv.org/abs/1711.05101

## 133. NORMALISATION ET DOCUMENTATION DES API

DIAPOSITIVE 133 — NORMALISATION ET DOCUMENTATION DES API

EXPLICATION TECHNIQUE
Ces références aident à vérifier les détails qui modifient réellement une implémentation. Les publications sur BatchNorm et LayerNorm expliquent les axes et les paramètres. L'analyse pre-LN/post-LN éclaire la place de la normalisation, sans remplacer une validation sur la configuration retenue. Les pages PyTorch consultées sont celles de la version 2.8 utilisée dans les dépendances des TP. En lisant une documentation d'API, vérifier les formes, les valeurs par défaut, la réduction d'une perte et le sens d'un masque booléen. Une signature familière peut cacher des conventions différentes.

QUESTION À POSER
Que vérifier avant de remplacer une attention manuelle par une API optimisée ?

RÉPONSE ATTENDUE
Les formes, la mise à l’échelle, les masques, le dropout et le sens des booléens.

LECTURES ET RÉFÉRENCES
Ioffe et Szegedy — Batch Normalization, 2015
https://arxiv.org/abs/1502.03167

Ba et al. — Layer Normalization, 2016
https://arxiv.org/abs/1607.06450

Xiong et al. — On Layer Normalization in the Transformer Architecture, 2020
https://arxiv.org/abs/2002.04745

PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

PyTorch 2.8 — CrossEntropyLoss
https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html

PyTorch 2.8 — MultiheadAttention
https://docs.pytorch.org/docs/2.8/generated/torch.nn.MultiheadAttention.html

## 134. VOTRE CHECKLIST TECHNIQUE

DIAPOSITIVE 134 — VOTRE CHECKLIST TECHNIQUE

EXPLICATION TECHNIQUE
Terminer par un retour sur les preuves de maîtrise annoncées en début de cours. Demander à chaque étudiant de choisir la compétence la moins solide et de formuler un exercice permettant de la renforcer. Les notebooks, les sources LaTeX et les notes du présentateur permettent de reprendre les démonstrations. Le meilleur prolongement consiste à garder un protocole simple et à augmenter progressivement la difficulté, plutôt qu'à passer directement à un modèle très grand. Une compréhension précise des formes, des objectifs et des masques se transfère à des architectures plus complexes.

QUESTION À POSER
Quelle partie savez-vous vérifier sans vous fier seulement à un score ?

RÉPONSE ATTENDUE
Les dimensions, le gradient, les invariants de l’attention et la séparation des données.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 135. MERCI

DIAPOSITIVE 135 — MERCI

EXPLICATION TECHNIQUE
Inviter les étudiants à revenir sur une équation, un résultat de TP ou une erreur observée. Pour chaque question, partir du problème et des hypothèses avant de choisir une architecture. La conclusion attendue est une capacité à expliquer un calcul, à construire une expérience et à reconnaître les limites de ce que les résultats démontrent. Les suites possibles sont un projet de vision sur données réelles, une étude de modèles préentraînés ou une analyse plus avancée de l'optimisation et des architectures séquentielles.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

