# Deep Learning — Guide du formateur

Master 2 IA · Chrys NIONGOLO · 35 heures, cinq journées.

Les mêmes explications figurent dans les notes de chaque diapositive du PowerPoint. Les équations sont rendues depuis LaTeX ; leur source est conservée ci-dessous et dans sources/formules.tex. Les pauses sont à ajouter aux 420 minutes quotidiennes.

## 1. DEEP LEARNING

DIAPOSITIVE 1 — DEEP LEARNING

EXPLICATION TECHNIQUE
Présenter les trois compétences visées : calculer et interpréter les gradients d'un réseau profond, construire un CNN adapté à un problème de vision et expliquer chaque opération d'un Transformer. Le fil conducteur est une même chaîne de raisonnement : définir les entrées et les sorties, écrire les opérations, choisir une perte, calculer ses gradients, puis vérifier la généralisation. Préciser que les petits modèles des TP servent à isoler les mécanismes. Ils ne reproduisent ni le coût ni les capacités d'un modèle de fondation.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 2. SOMMAIRE

DIAPOSITIVE 2 — SOMMAIRE

EXPLICATION TECHNIQUE
Le cours suit cinq journées de sept heures de formation effective, hors pauses. Chaque journée contient un TP exécuté sur CPU, des exercices mathématiques et une restitution. Les supports de Bigot, Tavenard, du CNAM et de Geoffrey Daniel servent de lectures complémentaires. Les articles originaux complètent la partie architectures. Les exemples numériques, exercices et notebooks de ce support sont construits pour cette progression. Inviter les étudiants à conserver un carnet des dimensions, hypothèses et observations.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

Geoffrey Daniel — Réseaux de neurones et deep learning : utilisation et méthodologie
https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf

## 3. OBJECTIFS ET PREUVES DE MAÎTRISE

Objectif | Preuve attendue
Rétropropagation | Dérivation, dimensions et contrôle numérique
CNN pour la vision | Architecture, entraînement et analyse des erreurs
Transfert | Comparaison source / cible et stratégies de gel
Transformer | Attention, masque causal et boucle autoregressive
Démarche expérimentale | Validation séparée, ablations et limites explicites

DIAPOSITIVE 3 — OBJECTIFS ET PREUVES DE MAÎTRISE

EXPLICATION TECHNIQUE
Une compétence est acquise lorsque l'étudiant peut justifier son résultat et diagnostiquer un échec. Pour la rétropropagation, une dérivée mémorisée ne suffit pas : il faut relier chaque facteur à une opération du calcul direct. Pour les CNN, contrôler les tailles et le nombre de paramètres avant l'entraînement. Pour les Transformers, reconstruire le chemin Q, K, V et expliquer ce que le masque interdit. Les productions des TP seront évaluées sur la validité du protocole, la justesse technique et l'interprétation, sans seuil arbitraire de précision.

QUESTION À POSER
Que prouve une bonne accuracy sur le jeu d’entraînement ?

RÉPONSE ATTENDUE
La capacité à ajuster ces exemples ; elle ne prouve pas la généralisation.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 4. PRÉREQUIS ET OUTILS

DIAPOSITIVE 4 — PRÉREQUIS ET OUTILS

EXPLICATION TECHNIQUE
Faire un diagnostic rapide : demander la forme de AB lorsque A est de taille 4 × 3 et B de taille 3 × 2, puis la dérivée de log(1 + exp(z)). Le cours introduit PyTorch en parallèle des équations ; la bibliothèque ne remplace pas la compréhension des gradients. Les cinq notebooks sont autonomes et leur configuration de référence utilise le CPU. Prévoir un environnement Python 3.12 avec les dépendances du fichier requirements.txt. Une première exécution ne nécessite aucun téléchargement de données : digits est fourni par scikit-learn et les séquences sont synthétiques.

QUESTION À POSER
Quelle est la dérivée de log(1 + exp(z)) ?

RÉPONSE ATTENDUE
La sigmoïde : exp(z)/(1+exp(z)).

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 5. CONVENTIONS DE NOTATION

DIAPOSITIVE 5 — CONVENTIONS DE NOTATION

EXPLICATION TECHNIQUE
Fixer les conventions dès le début évite la plupart des erreurs de transposition. Dans les dérivations portant sur un exemple, x et les activations sont des vecteurs colonnes ; W transforme une dimension d'entrée en une dimension de sortie. Dans les implémentations, le premier axe est le batch et chaque exemple est une ligne. La même transformation devient donc X W transposée. B désigne la taille du batch, n la longueur d'une séquence, d sa largeur, C le nombre de canaux et K le nombre de classes. Le symbole élément par élément est le produit de Hadamard.

ÉQUATION — SOURCE LATEX
\begin{aligned}x&\in\mathbb{R}^{d},\quad W_\ell\in\mathbb{R}^{d_\ell\times d_{\ell-1}}\\X&\in\mathbb{R}^{B\times d},\quad H_\ell=\phi(XW_\ell^\top+\mathbf{1}b_\ell^\top)\end{aligned}

QUESTION À POSER
Pourquoi W est-il transposé dans la version batch ?

RÉPONSE ATTENDUE
Parce que les exemples sont stockés en lignes, alors que la dérivation utilise des colonnes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 6. RÉSEAUX PROFONDS

DIAPOSITIVE 6 — RÉSEAUX PROFONDS

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 7. JOUR 1 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Cadrage | Pré requis, notation et formulation du problème | 45
Modélisation | MLP, activations et fonctions de perte | 90
Dérivations | Règle de la chaîne et gradients vectorisés | 75
TP 01 | MLP NumPy, gradient numérique et généralisation | 150
Restitution | Autograd, exercices et synthèse | 60

DIAPOSITIVE 7 — JOUR 1 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 8. APPRENDRE DES REPRÉSENTATIONS

DIAPOSITIVE 8 — APPRENDRE DES REPRÉSENTATIONS

EXPLICATION TECHNIQUE
Partir d'un exemple de vision : les valeurs des pixels ne sont pas directement les catégories recherchées. Le réseau ajuste plusieurs transformations pour rendre la décision finale plus simple. Éviter l'affirmation systématique selon laquelle une couche représente des contours puis des objets : c'est une intuition possible, pas une garantie pour tous les modèles. Une représentation dépend des données, de la perte et des contraintes d'architecture. Comparer largeur et profondeur : augmenter l'une ou l'autre modifie la capacité, mais aussi l'optimisation et le coût. La qualité se juge sur des données distinctes.

ÉQUATION — SOURCE LATEX
f_\theta=f_L\circ f_{L-1}\circ\cdots\circ f_1

QUESTION À POSER
Une architecture plus profonde est-elle toujours meilleure ?

RÉPONSE ATTENDUE
Non : capacité, optimisation, données disponibles et biais inductif interagissent.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

## 9. LE NEURONE DIFFÉRENTIABLE

DIAPOSITIVE 9 — LE NEURONE DIFFÉRENTIABLE

EXPLICATION TECHNIQUE
Distinguer le perceptron historique à seuil d'un neurone entraîné par gradient. Une fonction seuil n'a pas la dérivée utile souhaitée ; les réseaux modernes emploient des activations différentiables presque partout ou des conventions de sous-gradient. Le biais déplace la frontière sans imposer qu'elle passe par l'origine. Les poids ne sont pas des importances universelles : leur interprétation dépend de l'échelle des variables et des couches suivantes. Faire calculer z pour x=(2,-1), w=(0,5;1) et b=1 : z=1, puis appliquer une ReLU pour obtenir 1.

ÉQUATION — SOURCE LATEX
z=w^\top x+b,\qquad a=\phi(z)

QUESTION À POSER
Combien de paramètres pour une entrée de dimension d ?

RÉPONSE ATTENDUE
d poids et un biais, soit d+1.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 10. POURQUOI LA NON-LINÉARITÉ ?

DIAPOSITIVE 10 — POURQUOI LA NON-LINÉARITÉ ?

EXPLICATION TECHNIQUE
Développer le produit au tableau pour montrer exactement ce que l'empilement affine peut exprimer. On peut absorber deux couches dans une seule matrice et un seul biais. La représentation du XOR constitue un contre-exemple classique à une séparation linéaire dans l'espace d'entrée : ses classes occupent des coins opposés. Une couche cachée non linéaire transforme cet espace. Ne pas confondre ce constat avec les effets d'une factorisation linéaire sur l'optimisation ; ici, on parle de la classe de fonctions représentables, pas de la trajectoire suivie pendant l'entraînement.

ÉQUATION — SOURCE LATEX
W_2(W_1x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2)

QUESTION À POSER
Que devient un réseau de dix couches linéaires ?

RÉPONSE ATTENDUE
Une application affine unique, si des biais sont présents.

LECTURES ET RÉFÉRENCES
Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

## 11. ACTIVATIONS : VALEURS ET SATURATION

DIAPOSITIVE 11 — ACTIVATIONS : VALEURS ET SATURATION

EXPLICATION TECHNIQUE
Lire les deux courbes comme des fonctions scalaires appliquées composante par composante. La sigmoïde est utile pour une probabilité binaire en sortie ; dans des couches cachées profondes, sa saturation peut réduire fortement les gradients. ReLU évite la saturation sur la branche positive mais peut laisser certaines unités inactives pour tous les exemples. Une activation n'est donc pas choisie seulement pour son coût : il faut considérer l'initialisation et la distribution des préactivations. Les courbes présentées sont calculées directement à partir des définitions, sans mesures d'entraînement.

QUESTION À POSER
Quelle est la valeur de la sigmoïde en zéro ?

RÉPONSE ATTENDUE
0,5 ; sa dérivée en zéro vaut 0,25.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 12. DÉRIVÉES DES ACTIVATIONS

DIAPOSITIVE 12 — DÉRIVÉES DES ACTIVATIONS

EXPLICATION TECHNIQUE
Retrouver la dérivée de la sigmoïde par la dérivation d'un inverse et d'une exponentielle. Son maximum est 1/4, ce qui prépare l'analyse de l'atténuation des gradients, sans suffire à elle seule à décrire un réseau complet : les matrices de poids interviennent aussi. Pour ReLU, la dérivée n'existe pas au point zéro ; la valeur zéro utilisée dans nos calculs est une convention pratique. Φ est la fonction de répartition de la loi normale centrée réduite. GELU ne doit pas être confondue avec une probabilité de sortie : c'est une activation.

ÉQUATION — SOURCE LATEX
\sigma'(z)=\sigma(z)(1-\sigma(z)),\quad\phi_{\rm ReLU}'(z)=\mathbf{1}_{z>0}\\\operatorname{GELU}(z)=z\Phi(z)

QUESTION À POSER
La dérivée de ReLU vaut-elle 1 pour toute entrée ?

RÉPONSE ATTENDUE
Non : elle vaut zéro sur les entrées négatives.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 13. UNE COUCHE DENSE : FORMES ET CALCUL

DIAPOSITIVE 13 — UNE COUCHE DENSE : FORMES ET CALCUL

EXPLICATION TECHNIQUE
Écrire la forme de chaque objet : a précédent a d précédent composantes, W a d courant lignes et d précédent colonnes, b a d courant composantes. Le comptage inclut exactement un biais par neurone de sortie. Pour 784 entrées et 128 unités, la couche contient 784 × 128 + 128 = 100480 paramètres. Le nombre de paramètres ne dépend pas de B, même si la mémoire des activations et le coût du calcul en dépendent. Dans PyTorch, nn.Linear(in_features, out_features) stocke précisément une matrice out_features × in_features.

ÉQUATION — SOURCE LATEX
a_\ell=\phi_\ell(W_\ell a_{\ell-1}+b_\ell),\qquad P_\ell=d_\ell(d_{\ell-1}+1)

QUESTION À POSER
Une couche 64 → 10 contient combien de paramètres ?

RÉPONSE ATTENDUE
64×10+10 = 650.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 14. MLP : ARCHITECTURE ET PARAMÈTRES

Opération | Forme pour un batch B | Paramètres
Entrée | B × 2 | 0
Dense + ReLU | B × 16 | 2×16 + 16 = 48
Dense : logits | B × 2 | 16×2 + 2 = 34
Softmax pour lecture | B × 2 | 0
Total | 2 classes | 82

DIAPOSITIVE 14 — MLP : ARCHITECTURE ET PARAMÈTRES

EXPLICATION TECHNIQUE
Effectuer le comptage couche par couche, puis la somme. Pour l'exemple 2 → 16 → 2, la première couche comporte 32 poids et 16 biais ; la seconde 32 poids et 2 biais. Le réseau a donc 82 paramètres entraînables. Les activations ne portent pas de paramètres pour une ReLU ou une sigmoïde standard. Cette architecture sera utilisée dans le premier TP sur deux lunes. L'objectif est de relier les dimensions du code à une décision géométrique dans un espace de dimension deux, où le problème peut être visualisé sans réduction de dimension.

QUESTION À POSER
Changer le batch de 32 à 64 double-t-il les paramètres ?

RÉPONSE ATTENDUE
Non. Cela augmente le nombre d’activations conservées pendant le calcul.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 15. PERTE DE RÉGRESSION

DIAPOSITIVE 15 — PERTE DE RÉGRESSION

EXPLICATION TECHNIQUE
Développer la somme des carrés composante par composante. Le gradient a la même dimension que la sortie. Si le modèle surestime y, le signe du gradient est positif et une descente réduit la prédiction localement. Sous une hypothèse de bruit gaussien de variance constante, la minimisation des carrés a une interprétation de maximum de vraisemblance ; cette hypothèse n'est pas universelle. Certains logiciels divisent aussi par le nombre de composantes de sortie. Il faut donc vérifier la réduction utilisée avant de comparer une dérivation et les gradients d'une bibliothèque.

ÉQUATION — SOURCE LATEX
\ell(\hat y,y)=\frac12\|\hat y-y\|_2^2,\qquad\nabla_{\hat y}\ell=\hat y-y

QUESTION À POSER
Quel gradient obtient-on pour y=2 et une prédiction 5 ?

RÉPONSE ATTENDUE
3 avec la convention de cette diapositive.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 16. CLASSIFICATION : SOFTMAX ET ENTROPIE CROISÉE

DIAPOSITIVE 16 — CLASSIFICATION : SOFTMAX ET ENTROPIE CROISÉE

EXPLICATION TECHNIQUE
Pour une cible one-hot, un seul terme de la somme reste : moins le logarithme de la probabilité attribuée à la classe correcte. Deux sorties très différentes peuvent conduire à la même classe prédite mais à des pertes différentes, ce qui permet à l'optimiseur d'exploiter la confiance relative. Les probabilités produites ne sont pas automatiquement calibrées. Distinguer classification exclusive avec softmax et classification multi-label avec des sigmoïdes indépendantes. Les équations ci-dessus concernent des classes mutuellement exclusives et une distribution cible de somme un.

ÉQUATION — SOURCE LATEX
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}},\qquad\ell(z,y)=-\sum_{k=1}^{K}y_k\log p_k

QUESTION À POSER
Pourquoi accuracy et entropie croisée ne racontent-elles pas la même chose ?

RÉPONSE ATTENDUE
L’accuracy ne dépend que de l’argmax ; la perte dépend des probabilités.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — CrossEntropyLoss
https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html

## 17. STABILITÉ NUMÉRIQUE DES LOGITS

DIAPOSITIVE 17 — STABILITÉ NUMÉRIQUE DES LOGITS

EXPLICATION TECHNIQUE
Montrer l'invariance en multipliant numérateur et dénominateur par exp(-m). L'exemple z=(1000,1001) provoque un débordement si l'on calcule les exponentielles naïvement ; après translation, les arguments deviennent -1 et 0. En PyTorch, appliquer softmax avant CrossEntropyLoss change l'objet donné à la perte, qui attend déjà des logits et applique sa propre normalisation stable. Pour une classification binaire à une sortie, la version analogue est BCEWithLogitsLoss. La précision numérique est une contrainte d'implémentation qui doit être distinguée de la définition mathématique.

ÉQUATION — SOURCE LATEX
\ell(z,c)=-z_c+m+\log\sum_j e^{z_j-m},\qquad m=\max_j z_j

QUESTION À POSER
Faut-il appliquer softmax avant CrossEntropyLoss ?

RÉPONSE ATTENDUE
Non : fournir les logits et des étiquettes entières dans notre configuration.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — CrossEntropyLoss
https://docs.pytorch.org/docs/2.8/generated/torch.nn.CrossEntropyLoss.html

## 18. RISQUE EMPIRIQUE ET GÉNÉRALISATION

DIAPOSITIVE 18 — RISQUE EMPIRIQUE ET GÉNÉRALISATION

EXPLICATION TECHNIQUE
La fonction minimisée est une approximation du risque attendu sur de nouvelles données. Une faible erreur empirique ne suffit donc pas : le modèle peut mémoriser le bruit ou exploiter une fuite d'information. Le symbole approximation rappelle qu'un réseau non convexe est généralement optimisé par un nombre fini de mises à jour sans garantie d'atteindre un minimum global. Expliquer le rôle de chaque partition et insister sur l'apprentissage du prétraitement à partir du train seul. Une augmentation de données doit respecter la sémantique de la cible et ne jamais relier les partitions.

ÉQUATION — SOURCE LATEX
\hat R(\theta)=\frac1N\sum_{i=1}^{N}\ell(f_\theta(x_i),y_i),\qquad\hat\theta\approx\arg\min_\theta\hat R(\theta)

QUESTION À POSER
Où choisit-on le nombre d’époques ?

RÉPONSE ATTENDUE
À partir du train et de la validation, jamais du test.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

Geoffrey Daniel — Réseaux de neurones et deep learning : utilisation et méthodologie
https://indico.in2p3.fr/event/17858/attachments/49454/65831/Deep_Learning_Seance_1.pdf

## 19. DESCENTE DE GRADIENT

DIAPOSITIVE 19 — DESCENTE DE GRADIENT

EXPLICATION TECHNIQUE
Faire dériver un risque quadratique simple avant de parler de réseau. La rétropropagation calcule les dérivées ; SGD ou Adam utilisent ces dérivées pour choisir une mise à jour. Un pas trop grand peut augmenter la perte même si le gradient est correct. Un pas trop petit peut rendre la progression indétectable au budget disponible. Le sens de descente est une propriété locale à l'ordre un et ne constitue pas une preuve d'amélioration pour un pas fini. Les conditions théoriques de convergence dépendent de la régularité de la fonction et de la suite des pas.

ÉQUATION — SOURCE LATEX
\theta_{t+1}=\theta_t-\eta_t\nabla_\theta\hat R(\theta_t)

QUESTION À POSER
Un gradient correct garantit-il que chaque étape diminue la perte ?

RÉPONSE ATTENDUE
Non : le pas et l’approximation stochastique interviennent.

LECTURES ET RÉFÉRENCES
Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

## 20. RÈGLE DE LA CHAÎNE

DIAPOSITIVE 20 — RÈGLE DE LA CHAÎNE

EXPLICATION TECHNIQUE
Dessiner au tableau le graphe d'un calcul scalaire, puis identifier la valeur transportée vers l'avant et la sensibilité transportée vers l'arrière. Le gradient arrière d'un nœud est la variation de la perte due à une petite variation de ce nœud. Si une variable intervient dans plusieurs opérations, toutes ses contributions doivent être additionnées. C'est ce qui rend nécessaire l'accumulation, en particulier dans les connexions résiduelles et le partage de paramètres. On ne calcule pas un gradient différent pour chaque branche puis on n'en conserve qu'un seul.

ÉQUATION — SOURCE LATEX
z=g(x),\quad u=h(z),\quad \frac{\partial\ell}{\partial x}=\frac{\partial\ell}{\partial u}\frac{\partial u}{\partial z}\frac{\partial z}{\partial x}

QUESTION À POSER
Que fait-on si un paramètre est utilisé deux fois dans le graphe ?

RÉPONSE ATTENDUE
On somme les contributions de ses deux utilisations.

LECTURES ET RÉFÉRENCES
Javiera Castillo Navarro — RCP 209, 2025–2026
https://cedric.cnam.fr/vertigo/Cours/ml2/docs/coursDeep1.pdf

## 21. EXEMPLE SCALAIRE : UN PAS COMPLET

DIAPOSITIVE 21 — EXEMPLE SCALAIRE : UN PAS COMPLET

EXPLICATION TECHNIQUE
Calculer d'abord z=1, puis a=1/(1+exp(-1)). Le résidu est négatif car la sortie est inférieure à la cible. Sa multiplication par la dérivée de la sigmoïde, puis par x, donne un gradient d'environ -0,10575. Pour le biais, le même calcul omet le facteur x et donne environ -0,05288. La mise à jour produit w≈0,51058 et b≈0,00529. Recalculer ensuite la perte et vérifier qu'elle diminue pour ce pas précis. Cet exemple concerne une sigmoïde associée à une perte quadratique, et non la simplification softmax-entropie croisée présentée ensuite.

ÉQUATION — SOURCE LATEX
\ell=\tfrac12(a-y)^2,\quad a=\sigma(wx+b)\\\frac{\partial\ell}{\partial w}=(a-y)a(1-a)x\approx-0.1058

QUESTION À POSER
Quel facteur disparaît dans la dérivée par rapport au biais ?

RÉPONSE ATTENDUE
Le facteur x ; la dérivée de wx+b par rapport à b vaut 1.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 22. GRADIENT DE SOFTMAX + ENTROPIE CROISÉE

DIAPOSITIVE 22 — GRADIENT DE SOFTMAX + ENTROPIE CROISÉE

EXPLICATION TECHNIQUE
Développer moins la somme y_i log(p_i), puis appliquer la dérivée de chaque p_i par rapport à z_j. La somme des y_i vaut un ; on obtient p_j-y_j. Pour la bonne classe, le gradient est négatif tant que la probabilité n'atteint pas un ; pour les autres classes, il est positif. La somme des composantes du gradient vaut zéro, conformément à l'invariance de softmax à l'ajout d'une constante. Avec une moyenne sur B exemples, le facteur 1/B doit être appliqué une fois, soit ici soit dans l'agrégation, pas deux fois.

ÉQUATION — SOURCE LATEX
\frac{\partial p_i}{\partial z_j}=p_i(\delta_{ij}-p_j),\qquad\frac{\partial\ell}{\partial z}=p-y

QUESTION À POSER
Pourquoi les gradients des logits somment-ils à zéro ?

RÉPONSE ATTENDUE
Parce que les distributions p et y ont toutes deux une somme égale à un.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 23. RÉTROPROPAGATION D’UNE COUCHE DENSE

DIAPOSITIVE 23 — RÉTROPROPAGATION D’UNE COUCHE DENSE

EXPLICATION TECHNIQUE
Vérifier les dimensions avant de développer la dérivée. δ a d courant composantes et a précédent en a d précédent ; leur produit extérieur donne bien une matrice de même forme que W. Pour une composante W_ij, la sensibilité de z_i est a_j et celle de la perte par rapport à z_i est δ_i. Le biais est ajouté directement à z, d'où son gradient δ. Ces formules concernent un exemple unique. Le passage au batch se fait ensuite en additionnant ou en moyennant les contributions selon la réduction de la perte.

ÉQUATION — SOURCE LATEX
\delta_\ell=\frac{\partial\ell}{\partial z_\ell},\quad\nabla_{W_\ell}\ell=\delta_\ell a_{\ell-1}^{\top}\\\nabla_{b_\ell}\ell=\delta_\ell,\quad\frac{\partial\ell}{\partial a_{\ell-1}}=W_\ell^\top\delta_\ell

QUESTION À POSER
Pourquoi le gradient de W a-t-il la même forme que W ?

RÉPONSE ATTENDUE
Il contient une dérivée pour chacun de ses paramètres scalaires.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

## 24. PROPAGER LE SIGNAL DANS LES COUCHES CACHÉES

DIAPOSITIVE 24 — PROPAGER LE SIGNAL DANS LES COUCHES CACHÉES

EXPLICATION TECHNIQUE
La multiplication par W transposée distribue le signal d'erreur vers les unités de la couche précédente. Le produit de Hadamard filtre ensuite ce signal par la sensibilité locale de l'activation. Pour ReLU, les préactivations négatives ne transmettent aucun gradient par cette branche. Expliquer pourquoi il faut utiliser les poids du passage avant pour tout le passage arrière : mettre W à jour avant de calculer les gradients des couches précédentes mélangerait deux états du modèle. L'optimiseur intervient après que tous les gradients nécessaires ont été calculés.

ÉQUATION — SOURCE LATEX
\delta_\ell=\left(W_{\ell+1}^\top\delta_{\ell+1}\right)\odot\phi_\ell'(z_\ell)

QUESTION À POSER
Peut-on mettre les poids à jour pendant que l’on remonte les couches ?

RÉPONSE ATTENDUE
Pas dans la rétropropagation standard : on utilise un même état des poids.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 25. GRADIENTS VECTORISÉS SUR UN BATCH

DIAPOSITIVE 25 — GRADIENTS VECTORISÉS SUR UN BATCH

EXPLICATION TECHNIQUE
Prendre B=32, une entrée de largeur 16 et une sortie de largeur 10. H est 32×16, W est 10×16, Z et D sont 32×10. D transposée multipliée par H donne 10×16. Dans nos implémentations NumPy, D contient déjà la division par B issue de la perte moyenne ; on ne divise donc pas à nouveau le gradient des poids. Les biais sont broadcastés pendant le passage avant : le passage arrière doit inverser cette opération en sommant sur les axes répétés. Ce principe s'applique à de nombreux bugs d'autograd manuel.

ÉQUATION — SOURCE LATEX
Z=HW^\top+\mathbf1b^\top,\quad D=\frac{\partial\mathcal L}{\partial Z}\\\nabla_W\mathcal L=D^\top H,\quad\nabla_b\mathcal L=\sum_{i=1}^{B}D_{i,:},\quad\nabla_H\mathcal L=DW

QUESTION À POSER
Si D=(p-y)/B, faut-il encore diviser DᵀH par B ?

RÉPONSE ATTENDUE
Non : cela réduirait le gradient d’un facteur B supplémentaire.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 26. VÉRIFIER UN GRADIENT NUMÉRIQUEMENT

DIAPOSITIVE 26 — VÉRIFIER UN GRADIENT NUMÉRIQUEMENT

EXPLICATION TECHNIQUE
Une vérification numérique est un outil de diagnostic, pas une méthode pratique d'entraînement : elle exige deux évaluations de la perte par paramètre testé. Une valeur epsilon trop grande produit une erreur de troncature ; trop petite, une erreur d'arrondi. Une plage autour de 10 puissance moins cinq convient souvent en double précision, sans être une constante universelle. Désactiver le dropout et contrôler toute source d'aléa. Si la perturbation traverse zéro pour une ReLU, les dérivées peuvent différer sans que la règle de propagation soit incorrecte. Le TP vérifie séparément chaque tableau de paramètres.

ÉQUATION — SOURCE LATEX
g_j^{\rm num}=\frac{\mathcal L(\theta+\varepsilon e_j)-\mathcal L(\theta-\varepsilon e_j)}{2\varepsilon}\\r=\frac{\|g^{\rm num}-g\|_2}{\|g^{\rm num}\|_2+\|g\|_2+10^{-12}}

QUESTION À POSER
Pourquoi la différence finie est-elle coûteuse pour un grand réseau ?

RÉPONSE ATTENDUE
Son coût croît avec le nombre de paramètres vérifiés.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 27. AUTOGRAD : CE QUI EST AUTOMATISÉ

DIAPOSITIVE 27 — AUTOGRAD : CE QUI EST AUTOMATISÉ

EXPLICATION TECHNIQUE
Autograd applique un calcul de produits vecteur-Jacobienne en mode inverse, sans former toutes les Jacobiennes denses. Les activations nécessaires au passage arrière sont conservées, ce qui explique une partie de la mémoire d'entraînement. requires_grad indique quels tenseurs participent au calcul différentiel. detach coupe une relation dans le graphe, tandis qu'un contexte no_grad ou inference_mode évite d'enregistrer des opérations destinées à l'évaluation. Préciser que model.eval() change le comportement de certaines couches mais ne désactive pas, à lui seul, la construction du graphe. Les gradients s'accumulent tant qu'ils ne sont pas remis à zéro.

QUESTION À POSER
model.eval() désactive-t-il les gradients ?

RÉPONSE ATTENDUE
Non : utiliser aussi no_grad ou inference_mode pour l’évaluation.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 28. BOUCLE D’ENTRAÎNEMENT : INVARIANTS

DIAPOSITIVE 28 — BOUCLE D’ENTRAÎNEMENT : INVARIANTS

EXPLICATION TECHNIQUE
Faire verbaliser la distinction entre époque, batch et étape d'optimisation. Mélanger l'ordre du train d'une époque à l'autre est usuel ; conserver une évaluation déterministe facilite les comparaisons. La perte de l'époque doit être pondérée par le nombre d'exemples lorsque le dernier batch est incomplet, afin de ne pas lui attribuer un poids excessif. Vérifier les types : logits flottants et cibles entières pour une classification multiclasses. Avant une expérience longue, essayer de surapprendre quelques exemples, puis vérifier que le passage en mode évaluation ne modifie aucun poids.

QUESTION À POSER
Pourquoi pondérer les pertes de batches par leurs tailles ?

RÉPONSE ATTENDUE
Pour retrouver la vraie moyenne par exemple, même avec un dernier batch plus petit.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 29. TP 01 · UN MLP EN NUMPY

DIAPOSITIVE 29 — TP 01 · UN MLP EN NUMPY

EXPLICATION TECHNIQUE
Organisation : 20 minutes pour lire les données et les formes, 40 minutes pour annoter le calcul du gradient, 25 minutes pour le contrôle numérique, 40 minutes d'expériences et 25 minutes de restitution. Le notebook étudiant contient une base exécutable et des consignes d'investigation. Faire prédire l'effet d'un grand taux d'apprentissage avant de l'essayer. Les prétraitements sont ajustés sur le train. Les réponses doivent distinguer erreur d'implémentation, difficulté d'optimisation et manque de généralisation. Les corrigés proposent des conclusions attendues sans imposer un score unique.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Une configuration, une graine, des courbes, un contrôle du gradient et une limite identifiée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 30. DIAGNOSTIQUER AVANT D’AJOUTER DES COUCHES

Symptôme | Vérification prioritaire
Perte constante | Gradients, taux d’apprentissage, paramètres entraînables
NaN ou inf | Logits, normalisation, division et pas trop grand
Train bon, validation faible | Split, surapprentissage, décalage de distribution
Score presque parfait dès le début | Fuite de cible ou duplication train/test
Gradients NumPy ≠ numériques | Axes, transpose, facteur de moyenne et ReLU

DIAPOSITIVE 30 — DIAGNOSTIQUER AVANT D’AJOUTER DES COUCHES

EXPLICATION TECHNIQUE
Cette liste doit être appliquée dans l'ordre. Une erreur de forme, de cible ou de réduction peut produire une courbe qui ressemble à un mauvais choix d'hyperparamètre. Examiner ensuite les normes de gradients et la capacité à ajuster un très petit sous-ensemble. Si le train progresse mais pas la validation, l'optimisation fonctionne probablement : investiguer la régularisation, le protocole et les données. Une fuite de cible peut au contraire donner des résultats artificiellement excellents. Demander à chaque binôme d'associer un symptôme à une vérification falsifiable, plutôt qu'à une solution automatique.

QUESTION À POSER
Quelle première expérience distingue souvent un bug d’un problème de généralisation ?

RÉPONSE ATTENDUE
Essayer de surapprendre un très petit lot d’exemples.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 31. EXERCICE · RECONSTRUIRE LE GRADIENT

DIAPOSITIVE 31 — EXERCICE · RECONSTRUIRE LE GRADIENT

EXPLICATION TECHNIQUE
Accorder dix minutes de travail individuel puis mettre les propositions en commun. Pour un exemple colonne, W1 est 4×3, b1 est 4, a1 est 4, W2 est 2×4, b2 est 2. Le total est 12+4+8+2=26. La sortie a deux logits et delta2=p-y. Le gradient W2 est delta2 a1 transposée ; delta1=(W2 transposée delta2) multiplié élément par élément par l'indicatrice z1>0. Le gradient W1 est delta1 x transposée. Pour un batch, les activations passent en lignes et les produits changent d'ordre, sans changer le modèle.

QUESTION À POSER
Quel est le nombre total de paramètres ?

RÉPONSE ATTENDUE
26 : 16 dans la première couche et 10 dans la seconde.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 32. JOUR 1 · À RETENIR

DIAPOSITIVE 32 — JOUR 1 · À RETENIR

EXPLICATION TECHNIQUE
Clore la séance par une explication sans code : demander à un étudiant de décrire le trajet d'un exemple jusqu'à la perte, puis le trajet d'un gradient jusqu'à un poids de la première couche. Faire nommer le rôle du batch et de la moyenne. L'autre vérification consiste à faire calculer un gradient de biais et à expliquer pourquoi il est une somme dans la version vectorisée. Annoncer la journée suivante : une fois les gradients corrects, il reste à rendre l'optimisation stable et à utiliser une structure adaptée aux images.

QUESTION À POSER
Quelle opération est commune à tous les réseaux différentiables étudiés ?

RÉPONSE ATTENDUE
Composer des transformations et propager les sensibilités par la règle de la chaîne.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 33. OPTIMISATION ET CONVOLUTIONS

DIAPOSITIVE 33 — OPTIMISATION ET CONVOLUTIONS

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 34. JOUR 2 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Optimisation | Mini-batches, Adam, initialisation et régularisation | 90
CNN | Convolution, formes, paramètres et pooling | 105
Exercices | Calcul à la main et champ réceptif | 45
TP 02 | Petit CNN sur digits et expériences contrôlées | 150
Synthèse | Diagnostic et restitution | 30

DIAPOSITIVE 34 — JOUR 2 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 35. SGD ET MINI-BATCHES

DIAPOSITIVE 35 — SGD ET MINI-BATCHES

EXPLICATION TECHNIQUE
Le gradient de mini-batch est un estimateur du gradient empirique lorsque l'échantillonnage est approprié. Sa variabilité influence la trajectoire de l'optimisation, sans constituer une garantie de meilleure généralisation. Doubler le batch réduit le nombre d'étapes par époque ; comparer seulement le nombre d'époques peut donc masquer un changement de budget de mises à jour. La mémoire des activations croît avec B, alors que celle des paramètres reste fixe. Les relations simples de redimensionnement du taux d'apprentissage sont des heuristiques qui nécessitent une validation.

ÉQUATION — SOURCE LATEX
g_t=\frac1B\sum_{i\in\mathcal B_t}\nabla_\theta\ell_i(\theta_t),\qquad\theta_{t+1}=\theta_t-\eta_tg_t

QUESTION À POSER
Si N=1000 et B=128 sans drop_last, combien d’étapes par époque ?

RÉPONSE ATTENDUE
8, dont une dernière étape de 104 exemples.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 36. MOMENTUM : MÉMORISER UNE DIRECTION

DIAPOSITIVE 36 — MOMENTUM : MÉMORISER UNE DIRECTION

EXPLICATION TECHNIQUE
Présenter explicitement la convention employée : ici, on n'introduit pas le facteur 1-beta devant g. Une autre écriture utilise une moyenne exponentielle normalisée et nécessite un taux effectif différent. Lorsque les gradients gardent un même signe, leur contribution s'accumule et accélère le mouvement ; lorsqu'ils oscillent, une partie se compense. Une mémoire importante peut aussi provoquer un dépassement ou retarder un changement de direction. Le momentum n'élimine donc pas le choix du taux d'apprentissage. Initialiser v à zéro et calculer deux étapes pour un gradient constant.

ÉQUATION — SOURCE LATEX
v_t=\beta v_{t-1}+g_t,\qquad\theta_{t+1}=\theta_t-\eta v_t

QUESTION À POSER
Avec β=0,9, v0=0 et g=1, quelles sont v1 et v2 ?

RÉPONSE ATTENDUE
1 puis 1,9 dans cette convention.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 37. ADAM : PREMIER ET SECOND MOMENTS

DIAPOSITIVE 37 — ADAM : PREMIER ET SECOND MOMENTS

EXPLICATION TECHNIQUE
Le second moment est une moyenne des carrés, pas directement une estimation de variance centrée. La normalisation produit des échelles de pas différentes selon les coordonnées. Expliquer les facteurs de correction en développant l'espérance de m_t pour un gradient stationnaire : son initialisation à zéro réduit sa magnitude au début. Adam n'exonère pas du réglage du taux ni du contrôle des gradients. Les choix usuels des coefficients sont des points de départ et non des constantes mathématiques. Distinguer la stabilisation numérique epsilon d'une pénalisation du modèle.

ÉQUATION — SOURCE LATEX
\begin{aligned}m_t&=\beta_1m_{t-1}+(1-\beta_1)g_t\\v_t&=\beta_2v_{t-1}+(1-\beta_2)g_t^2\\\theta_{t+1}&=\theta_t-\eta\frac{m_t/(1-\beta_1^t)}{\sqrt{v_t/(1-\beta_2^t)}+\varepsilon}\end{aligned}

QUESTION À POSER
Le v d’Adam est-il exactement la variance du gradient ?

RÉPONSE ATTENDUE
Non : c’est un second moment non centré.

LECTURES ET RÉFÉRENCES
Kingma et Ba — Adam, 2014
https://arxiv.org/abs/1412.6980

## 38. INITIALISATION ET PROPAGATION DES VARIANCES

DIAPOSITIVE 38 — INITIALISATION ET PROPAGATION DES VARIANCES

EXPLICATION TECHNIQUE
L'argument de variance suppose approximativement des composantes indépendantes et centrées. Une somme de d contributions indépendantes additionne leurs variances ; il faut donc compenser l'augmentation de fan-in. ReLU élimine une partie du signal, d'où le facteur deux dans l'heuristique de He. Ces conditions idéalisées ne prouvent pas la stabilité de tout réseau réel, mais fournissent un point de départ utile. Les biais peuvent être initialisés à zéro sans rendre tous les neurones identiques si les poids sont aléatoires. Ne pas dire que tous les paramètres doivent nécessairement être aléatoires.

ÉQUATION — SOURCE LATEX
W_{ij}\sim\mathcal N\!\left(0,\frac{2}{d_{\rm in}}\right)\quad\text{(ReLU)},\qquad\operatorname{Var}(W_{ij})\approx\frac{2}{d_{\rm in}+d_{\rm out}}\quad\text{(Xavier)}

QUESTION À POSER
Pourquoi ne pas initialiser tous les poids d’une couche à la même valeur ?

RÉPONSE ATTENDUE
Les neurones peuvent rester symétriques et apprendre des représentations identiques.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 39. GRADIENTS QUI DISPARAISSENT OU EXPLOSENT

DIAPOSITIVE 39 — GRADIENTS QUI DISPARAISSENT OU EXPLOSENT

EXPLICATION TECHNIQUE
Une succession d'opérateurs contractants peut atténuer le signal, tandis que des directions amplifiées peuvent le faire exploser. Les normes spectrales donnent une intuition, mais la direction effective du gradient et les corrélations entre matrices comptent aussi. Le clipping par norme limite la magnitude d'un gradient déjà calculé ; il ne restaure pas un gradient disparu et ne corrige pas un masque erroné. Observer les normes par couche avant de proposer une intervention. Les connexions résiduelles introduisent un chemin identité, que nous retrouverons dans ResNet et dans les Transformers.

ÉQUATION — SOURCE LATEX
\frac{\partial\ell}{\partial a_0}=J_1^\top J_2^\top\cdots J_L^\top\frac{\partial\ell}{\partial a_L}

QUESTION À POSER
Le clipping permet-il de récupérer des gradients proches de zéro ?

RÉPONSE ATTENDUE
Non : il borne les grands gradients, il ne recrée pas les petits.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 40. PÉNALISATION L2 ET WEIGHT DECAY

DIAPOSITIVE 40 — PÉNALISATION L2 ET WEIGHT DECAY

EXPLICATION TECHNIQUE
Pour SGD sans adaptation, développer la mise à jour donne (1-eta lambda) theta moins eta fois le gradient de données. Avec Adam, introduire lambda theta dans le gradient modifie aussi les estimations des moments ; ce n'est donc pas en général la même opération qu'une décroissance séparée du paramètre. AdamW effectue ce découplage. En pratique, certains groupes de paramètres, tels que les biais ou les gains de normalisation, peuvent recevoir des réglages différents. Ce choix doit être documenté dans une comparaison. La pénalisation peut aider mais ne remplace pas un protocole de validation valide.

ÉQUATION — SOURCE LATEX
\mathcal L_{\rm reg}=\mathcal L+\frac\lambda2\|\theta\|_2^2,\qquad\nabla\mathcal L_{\rm reg}=\nabla\mathcal L+\lambda\theta

QUESTION À POSER
L2 et weight decay sont-ils interchangeables dans toutes les méthodes ?

RÉPONSE ATTENDUE
Non, notamment avec les optimiseurs adaptatifs.

LECTURES ET RÉFÉRENCES
Loshchilov et Hutter — Decoupled Weight Decay Regularization, 2017
https://arxiv.org/abs/1711.05101

## 41. DROPOUT : TRAIN ET ÉVALUATION

DIAPOSITIVE 41 — DROPOUT : TRAIN ET ÉVALUATION

EXPLICATION TECHNIQUE
La formule utilise p comme probabilité de suppression. Vérifier cette convention, car certaines présentations utilisent au contraire une probabilité de conservation. La conservation de l'espérance d'une activation ne signifie pas que l'espérance de toute la sortie du réseau est inchangée : les couches suivantes sont non linéaires. Un taux trop fort peut empêcher l'ajustement du train. Pour une vérification numérique des gradients, le masque doit rester fixe ou le dropout doit être désactivé. En PyTorch, train() et eval() pilotent ce comportement sans modifier automatiquement requires_grad.

ÉQUATION — SOURCE LATEX
m_j\sim\operatorname{Bernoulli}(1-p),\qquad\tilde a_j=\frac{m_j}{1-p}a_j,\qquad\mathbb E[\tilde a_j]=a_j

QUESTION À POSER
Pourquoi diviser par 1-p pendant le train ?

RÉPONSE ATTENDUE
Pour conserver l’espérance de l’activation dans le dropout inversé.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 42. NORMALISER LES ACTIVATIONS

DIAPOSITIVE 42 — NORMALISER LES ACTIVATIONS

EXPLICATION TECHNIQUE
Le point essentiel est de demander sur quels axes sont calculés moyenne et variance. BatchNorm utilise des statistiques regroupant plusieurs exemples et éventuellement des positions spatiales ; LayerNorm travaille à l'intérieur d'un exemple ou d'un token sur ses caractéristiques. Gamma et beta sont appris par gradient et ont des formes dépendant de la normalisation. Epsilon rend la division définie et influence le comportement lorsque la variance est très faible. Il faut distinguer ces normalisations internes du prétraitement global des entrées et des statistiques mobiles utilisées par BatchNorm à l'évaluation.

ÉQUATION — SOURCE LATEX
\hat x=\frac{x-\mu}{\sqrt{\sigma^2+\varepsilon}},\qquad y=\gamma\hat x+\beta

QUESTION À POSER
Peut-on comparer BatchNorm et LayerNorm sans préciser les axes ?

RÉPONSE ATTENDUE
Non : les axes définissent l’opération.

LECTURES ET RÉFÉRENCES
Ioffe et Szegedy — Batch Normalization, 2015
https://arxiv.org/abs/1502.03167

Ba et al. — Layer Normalization, 2016
https://arxiv.org/abs/1607.06450

## 43. EARLY STOPPING ET COURBES D’APPRENTISSAGE

DIAPOSITIVE 43 — EARLY STOPPING ET COURBES D’APPRENTISSAGE

EXPLICATION TECHNIQUE
Les courbes de cette diapositive sont illustratives et non les résultats d'un benchmark. Elles montrent un cas où la perte train continue de diminuer alors que la validation remonte. La règle d'arrêt doit préciser le critère, la direction d'amélioration, la patience et le changement minimal considéré. Sauvegarder réellement le meilleur état des poids, pas seulement l'indice de la meilleure époque. Tester plusieurs règles sur le même test revient à l'utiliser pour la sélection. Une seule séparation ne mesure pas toute la variabilité ; répéter sur plusieurs graines peut être utile si le budget le permet.

QUESTION À POSER
Pourquoi restaurer le meilleur checkpoint ?

RÉPONSE ATTENDUE
La dernière époque n’est pas nécessairement celle qui généralise le mieux.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 44. POURQUOI UN CNN POUR UNE IMAGE ?

DIAPOSITIVE 44 — POURQUOI UN CNN POUR UNE IMAGE ?

EXPLICATION TECHNIQUE
Comparer une image à un vecteur aplati. Une couche dense peut en principe apprendre des relations entre pixels, mais elle ne reçoit pas explicitement l'hypothèse qu'un motif local est réutilisable dans l'espace. La convolution introduit cette hypothèse dans la paramétrisation. Le partage réduit le nombre de paramètres et crée une équivariance sous certaines conditions. Il ne garantit pas l'invariance aux translations du modèle complet. Les effets de bord, le stride, le pooling et les couches finales peuvent modifier cette propriété. L'utilité du biais inductif dépend de la tâche et des transformations pertinentes.

QUESTION À POSER
Pourquoi le même noyau est-il appliqué à plusieurs positions ?

RÉPONSE ATTENDUE
Pour partager un détecteur local et ses paramètres dans l’espace.

LECTURES ET RÉFÉRENCES
Jérémie Bigot — Introduction au Deep Learning
https://www.math.u-bordeaux.fr/~jbigot/Site/Enseignement_files/Intro_DeepLearning.pdf

## 45. CONVOLUTION 2D : L’OPÉRATION LOCALE

DIAPOSITIVE 45 — CONVOLUTION 2D : L’OPÉRATION LOCALE

EXPLICATION TECHNIQUE
La formule correspond au cas stride un, sans dilation et sans padding, avec un batch omis pour la lisibilité. Une convolution mathématique retourne le noyau ; l'opération usuelle des couches Conv2d est une corrélation croisée. Puisque les coefficients sont appris, cette convention ne réduit pas la famille de détecteurs représentable. Chaque canal de sortie possède un ensemble de noyaux sur tous les canaux d'entrée et un biais. Un filtre RGB a donc trois plans de coefficients, pas un seul noyau recopié mécaniquement sur rouge, vert et bleu.

ÉQUATION — SOURCE LATEX
Y_{o,i,j}=b_o+\sum_{c=1}^{C_{\rm in}}\sum_{u=0}^{k_h-1}\sum_{v=0}^{k_w-1}W_{o,c,u,v}\,X_{c,i+u,j+v}

QUESTION À POSER
Un filtre 3×3 sur une entrée RGB contient-il 9 poids ?

RÉPONSE ATTENDUE
Non : il contient 3×3×3 = 27 poids, plus un biais éventuel.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

## 46. CONVOLUTION : EXEMPLE À LA MAIN

DIAPOSITIVE 46 — CONVOLUTION : EXEMPLE À LA MAIN

EXPLICATION TECHNIQUE
Faire remplir les quatre cases avant d'afficher le calcul oralement. La première vaut 1×1+2×0+0×0+1×(-1)=0. La deuxième vaut 2-3=-1, la troisième 0-1=-1 et la quatrième 1-0=1. Insister sur le fait qu'un seul jeu de quatre poids a produit toutes les sorties. Un biais s'ajouterait à chaque case du même canal. Ce noyau est fixé à titre pédagogique ; dans un CNN, il est généralement appris. Le calcul est une corrélation croisée valide et ne doit pas être mélangé à une convention de noyau retourné.

ÉQUATION — SOURCE LATEX
X=\begin{bmatrix}1&2&0\\0&1&3\\2&1&0\end{bmatrix},\quad W=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\\Y=\begin{bmatrix}0&-1\\-1&1\end{bmatrix}

QUESTION À POSER
Combien de paramètres seraient appris avec un biais ?

RÉPONSE ATTENDUE
5 : quatre poids et un biais.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 47. STRIDE, PADDING ET DILATION

DIAPOSITIVE 47 — STRIDE, PADDING ET DILATION

EXPLICATION TECHNIQUE
Définir le noyau effectif : d(k-1)+1. On compte ensuite le nombre de positions valides de cette fenêtre après ajout du padding. La formule présentée utilise un padding symétrique et s'applique indépendamment à la hauteur et à la largeur. Pour H=32, k=3, p=1, d=1 et s=2, la sortie vaut 16. Un padding dit same ne signifie pas la même chose pour tous les strides et toutes les bibliothèques ; dans les versions étudiées, vérifier les contraintes de l'API. La dilation augmente le champ couvert sans augmenter le nombre de coefficients.

ÉQUATION — SOURCE LATEX
H_{\rm out}=\left\lfloor\frac{H+2p-d(k-1)-1}{s}+1\right\rfloor

QUESTION À POSER
Pour H=28, k=3, p=0, s=1, d=1, quelle hauteur ?

RÉPONSE ATTENDUE
26.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

## 48. CANAUX ET TENSEURS D’UN CNN

Objet | Forme | Rôle
Entrée | B × Cᵢₙ × H × W | Images du batch
Poids | Cₒᵤₜ × Cᵢₙ × kₕ × k𝓌 | Détecteurs partagés
Biais | Cₒᵤₜ | Décalage par canal de sortie
Sortie | B × Cₒᵤₜ × Hₒᵤₜ × Wₒᵤₜ | Cartes de caractéristiques

DIAPOSITIVE 48 — CANAUX ET TENSEURS D’UN CNN

EXPLICATION TECHNIQUE
Conserver le batch au premier axe évite de confondre nombre d'images et nombre de canaux. Dans notre convention PyTorch, l'image est B×C×H×W. Une autre bibliothèque peut utiliser B×H×W×C ; l'algèbre est la même mais les axes à manipuler changent. Une convolution de 3 canaux vers 16 canaux produit 16 cartes d'activation, chacune agrégeant les trois canaux d'entrée. La notion de canal de sortie ne signifie pas que ce canal correspond à une classe ; les classes n'apparaissent que dans la tête finale choisie pour la tâche.

QUESTION À POSER
Une carte de caractéristiques correspond-elle nécessairement à une catégorie ?

RÉPONSE ATTENDUE
Non : c’est une représentation intermédiaire apprise.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 49. TAILLES ET NOMBRE DE PARAMÈTRES

DIAPOSITIVE 49 — TAILLES ET NOMBRE DE PARAMÈTRES

EXPLICATION TECHNIQUE
Pour une entrée RGB et 16 filtres 3×3, le nombre de paramètres est 16(3×9+1)=448. Les MACs comptent ici les multiplications-accumulations d'un exemple et omettent les biais. Une convention FLOPs peut compter deux opérations pour une multiplication-accumulation ; il faut annoncer cette convention. Si H et W doublent, les paramètres restent inchangés mais le calcul et les activations sont approximativement multipliés par quatre. Pour des convolutions groupées, le nombre de connexions par canal change ; la formule de cette diapositive doit alors être adaptée.

ÉQUATION — SOURCE LATEX
P=C_{\rm out}(C_{\rm in}k_hk_w+1)\\\operatorname{MACs}\approx H_{\rm out}W_{\rm out}C_{\rm out}C_{\rm in}k_hk_w

QUESTION À POSER
Une convolution contient-elle plus de poids lorsqu’on passe de 32×32 à 64×64 ?

RÉPONSE ATTENDUE
Non, à noyau et nombres de canaux constants.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — Conv2d
https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv2d.html

## 50. POOLING : RÉDUIRE LA RÉSOLUTION

DIAPOSITIVE 50 — POOLING : RÉDUIRE LA RÉSOLUTION

EXPLICATION TECHNIQUE
Expliquer la différence du passage arrière : le max transmet le gradient à une position sélectionnée, tandis que la moyenne le répartit également sur toutes les positions. Les égalités au maximum nécessitent une convention d'implémentation. Le sous-échantillonnage réduit la mémoire et augmente le champ réceptif des couches suivantes, mais détruit de l'information de position. Il ne procure pas une invariance parfaite aux translations. Une convolution à stride supérieur à un peut jouer un rôle de réduction de résolution tout en apprenant sa transformation, avec un autre coût en paramètres.

ÉQUATION — SOURCE LATEX
\operatorname{maxpool}\!\begin{bmatrix}1&4\\2&3\end{bmatrix}=4,\qquad\operatorname{avgpool}\!\begin{bmatrix}1&4\\2&3\end{bmatrix}=2.5

QUESTION À POSER
Où va le gradient d’un max pooling 2×2 sans égalité ?

RÉPONSE ATTENDUE
Vers l’entrée qui a produit le maximum.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 51. CHAMP RÉCEPTIF : CALCUL RÉCURSIF

DIAPOSITIVE 51 — CHAMP RÉCEPTIF : CALCUL RÉCURSIF

EXPLICATION TECHNIQUE
Faire le calcul pour Conv3 stride1, Pool2 stride2, Conv3 stride1. Après la première convolution, r=3 et j=1 ; après le pooling, r=4 et j=2 ; après la seconde convolution, r=8 et j=2. Deux convolutions 3×3 à stride un donnent en revanche un champ de 5×5 avant tout pooling. Le padding déplace les centres et traite les bords, mais n'augmente pas le nombre de pixels réels disponibles en dehors de l'image. Le champ réceptif effectif décrit les influences effectivement importantes, qui dépendent des poids et des données.

ÉQUATION — SOURCE LATEX
j_\ell=j_{\ell-1}s_\ell,\qquad r_\ell=r_{\ell-1}+(k_\ell-1)d_\ell j_{\ell-1}\\r_0=j_0=1

QUESTION À POSER
Quel champ obtient-on avec deux convolutions 3×3 sans stride ?

RÉPONSE ATTENDUE
5×5 dans le cas standard.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 52. ÉQUIVARIANCE ET INVARIANCE

DIAPOSITIVE 52 — ÉQUIVARIANCE ET INVARIANCE

EXPLICATION TECHNIQUE
Sur un domaine infini ou avec des conditions adaptées, une convolution à stride un commute avec une translation entière. Sur une image finie, le padding et les bords limitent cette égalité. Avec un stride supérieur à un, seules certaines translations s'alignent sur la grille de sous-échantillonnage. Un classifieur peut rechercher une certaine invariance via l'agrégation spatiale ou l'augmentation, mais cela n'est pas une conséquence absolue du mot CNN. Pour la segmentation, on souhaite plutôt préserver une relation spatiale entre entrée et sortie ; l'invariance totale serait indésirable.

ÉQUATION — SOURCE LATEX
f(Tx)=T f(x)\quad\text{(equivariance)},\qquad g(Tx)=g(x)\quad\text{(invariance)}

QUESTION À POSER
Une segmentation d’image doit-elle être totalement invariante à la translation ?

RÉPONSE ATTENDUE
Non : le masque devrait généralement se déplacer avec les objets.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 53. TP 02 · CONSTRUIRE UN PETIT CNN

DIAPOSITIVE 53 — TP 02 · CONSTRUIRE UN PETIT CNN

EXPLICATION TECHNIQUE
Déroulé : 20 minutes pour le protocole de séparation, 30 minutes pour les dimensions, 40 minutes pour l'entraînement, 35 minutes pour une ablation et 25 minutes d'analyse. Le réseau de base emploie deux blocs convolution-ReLU-pooling puis une tête dense. Les images sont divisées par 16, échelle définie par le jeu, sans apprentissage sur le test. Les étudiants comparent par exemple le pooling et une réduction par stride, à budget documenté. La petite résolution permet de travailler sur CPU ; les conclusions ne doivent pas être extrapolées directement à des images haute résolution.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Une architecture annotée, un protocole sans fuite et une explication de ses erreurs.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 54. EXERCICE · AUDITER UNE CONVOLUTION

DIAPOSITIVE 54 — EXERCICE · AUDITER UNE CONVOLUTION

EXPLICATION TECHNIQUE
Laisser huit minutes puis faire corriger par un autre binôme. H sortie et W sortie valent chacun floor((32+2-2-1)/2+1)=16. La forme est donc B×16×16×16. Le nombre de paramètres est 16(3×3×3+1)=448. Le coût principal vaut 16×16×16×3×3×3=110592 MACs par image, hors biais et activation. Le batch multiplie ce coût par B sans modifier le nombre de poids. Demander enfin l'effet d'un padding nul : la hauteur devient 15, ce qui modifie le calcul et les activations mais pas les paramètres.

QUESTION À POSER
Combien de MACs, hors biais et activation ?

RÉPONSE ATTENDUE
110 592 par image dans la convention indiquée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 55. JOUR 2 · À RETENIR

DIAPOSITIVE 55 — JOUR 2 · À RETENIR

EXPLICATION TECHNIQUE
Demander une restitution qui relie les deux moitiés de la journée. Les CNN n'ont pas une règle d'apprentissage séparée : ils utilisent la même rétropropagation, avec une structure de partage des poids. Le gradient d'un noyau additionne les contributions de toutes les positions où il a été appliqué et de tous les exemples du batch. Revenir sur le rôle des augmentations et du test pour ne pas confondre une hypothèse d'architecture et une propriété empiriquement validée. La journée suivante introduit le transfert, qui permet de réutiliser des représentations déjà apprises.

QUESTION À POSER
Comment le gradient d’un noyau combine-t-il ses multiples utilisations ?

RÉPONSE ATTENDUE
Il additionne les contributions des positions et des exemples.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 56. CNN ET TRANSFERT

DIAPOSITIVE 56 — CNN ET TRANSFERT

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 57. JOUR 3 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Architectures | CNN complet, BatchNorm et résidus | 60
Données | Augmentation, séparation et métriques | 75
Transfert | Gel, adaptation et expériences comparables | 75
TP 03 | Source digits 0–4 vers cible digits 5–9 | 180
Restitution | Erreurs, résultats et limites | 30

DIAPOSITIVE 57 — JOUR 3 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 58. LE CNN DU TP : PARCOURS D’UN BATCH

Étape | Forme hors batch | Paramètres
Conv 3×3 + ReLU | 8 × 8 × 8 | 80
MaxPool 2×2 | 8 × 4 × 4 | 0
Conv 3×3 + ReLU | 16 × 4 × 4 | 1 168
MaxPool + flatten | 64 | 0
Linear 64 → 10 | 10 logits | 650
Total |  | 1 898

DIAPOSITIVE 58 — LE CNN DU TP : PARCOURS D’UN BATCH

EXPLICATION TECHNIQUE
Ce tableau correspond exactement au réseau des notebooks. Une première convolution 1→8 conserve 8×8 grâce au padding, puis un pooling divise la résolution par deux. Le deuxième bloc 8→16 réduit ensuite 4×4 en 2×2. L'aplatissement donne 16×2×2=64 composantes. Le nombre de paramètres est 80+1168+650=1898 ; ReLU, pooling et flatten n'ajoutent aucun poids. Vérifier ce total avec la somme numel des paramètres PyTorch. L'aplatissement impose ici une taille d'entrée déterminée ; une agrégation globale pourrait rendre la tête moins dépendante de cette taille.

QUESTION À POSER
Pourquoi la tête reçoit-elle 64 entrées ?

RÉPONSE ATTENDUE
16 canaux × 2 × 2 positions.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 59. CONVOLUTION 1×1 ET AGRÉGATION GLOBALE

DIAPOSITIVE 59 — CONVOLUTION 1×1 ET AGRÉGATION GLOBALE

EXPLICATION TECHNIQUE
Un noyau 1×1 n'est pas une opération inutile : il réalise une projection sur les canaux, avec les mêmes poids à chaque position. Il est employé pour réduire ou augmenter la dimension et pour aligner les branches résiduelles. L'agrégation globale par moyenne réduit la dépendance de la tête à la taille spatiale et peut réduire fortement le nombre de paramètres. Elle détruit toutefois la localisation fine ; ce choix convient plus naturellement à certaines tâches de classification qu'à une reconstruction dense. Comparer son coût à celui d'une grande couche dense après aplatissement.

ÉQUATION — SOURCE LATEX
Y_{o,i,j}=b_o+\sum_c W_{o,c}X_{c,i,j},\qquad g_c=\frac1{HW}\sum_{i,j}X_{c,i,j}

QUESTION À POSER
Une convolution 1×1 peut-elle modifier le nombre de canaux ?

RÉPONSE ATTENDUE
Oui, via une projection apprise partagée à chaque position.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 60. BATCHNORM DANS UN CNN

DIAPOSITIVE 60 — BATCHNORM DANS UN CNN

EXPLICATION TECHNIQUE
Décrire précisément les axes d'agrégation pour une couche BatchNorm2d. Les paramètres gamma et beta possèdent une composante par canal et ne sont pas les statistiques mobiles. Les premières sont apprises par gradient ; les secondes sont des buffers mis à jour selon le comportement de la couche. Il existe des conventions d'estimation de variance et de mise à jour propres à chaque API ; la formule illustre ici la normalisation du batch. Durant un transfert sur peu de données, adapter ces statistiques peut être nuisible même si les poids convolutionnels sont gelés. D'où l'importance de distinguer gel des paramètres et mode évaluation.

ÉQUATION — SOURCE LATEX
\mu_c=\frac1{BHW}\sum_{b,i,j}X_{b,c,i,j},\quad\hat X_{b,c,i,j}=\frac{X_{b,c,i,j}-\mu_c}{\sqrt{\sigma_c^2+\varepsilon}}

QUESTION À POSER
requires_grad=False fige-t-il automatiquement les statistiques mobiles ?

RÉPONSE ATTENDUE
Non : elles dépendent aussi du mode train/eval de BatchNorm.

LECTURES ET RÉFÉRENCES
Ioffe et Szegedy — Batch Normalization, 2015
https://arxiv.org/abs/1502.03167

## 61. CONNEXIONS RÉSIDUELLES

DIAPOSITIVE 61 — CONNEXIONS RÉSIDUELLES

EXPLICATION TECHNIQUE
L'écriture résiduelle change la paramétrisation d'un bloc : F peut apprendre une petite correction ou se rapprocher de zéro. Le terme identité offre un chemin direct au signal et au gradient, sans garantir l'absence de toute difficulté d'optimisation. Si le nombre de canaux ou la résolution change, une projection P(x), souvent convolution 1×1 avec stride approprié, remplace l'identité pour rendre l'addition possible. Le gradient du paramètre d'une branche est calculé comme précédemment ; le gradient par rapport à l'entrée additionne les chemins. Cette structure sera centrale dans les blocs Transformers.

ÉQUATION — SOURCE LATEX
y=x+F(x),\qquad\frac{\partial y}{\partial x}=I+\frac{\partial F}{\partial x}

QUESTION À POSER
Peut-on ajouter directement B×16×16×16 et B×32×8×8 ?

RÉPONSE ATTENDUE
Non : il faut aligner les dimensions par une projection adaptée.

LECTURES ET RÉFÉRENCES
He et al. — Deep Residual Learning for Image Recognition, 2015
https://arxiv.org/abs/1512.03385

## 62. AUGMENTER SANS CHANGER LA CIBLE

DIAPOSITIVE 62 — AUGMENTER SANS CHANGER LA CIBLE

EXPLICATION TECHNIQUE
Une rotation légère peut être acceptable pour certains chiffres, mais une rotation de 180 degrés peut échanger des significations. Un retournement horizontal peut être adapté à une photographie d'objet et incorrect pour du texte. Pour une segmentation, il faut transformer la cible spatiale de façon cohérente. La formule suppose ici que T conserve la classe ; cette hypothèse doit être vérifiée. Une augmentation ne crée pas un nouvel individu indépendant pour le test : toutes les variantes d'une même observation doivent rester dans la même partition. Documenter la politique et ses probabilités dans le compte rendu.

ÉQUATION — SOURCE LATEX
\mathcal L_{\rm aug}=\mathbb E_{(x,y)}\,\mathbb E_{T\sim\mathcal A}\!\left[\ell(f_\theta(Tx),y)\right]

QUESTION À POSER
Pourquoi ne pas répartir des augmentations d’une même image entre train et test ?

RÉPONSE ATTENDUE
Cela crée une dépendance et une fuite entre les partitions.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 63. LE JEU DE DONNÉES FAIT PARTIE DU MODÈLE

DIAPOSITIVE 63 — LE JEU DE DONNÉES FAIT PARTIE DU MODÈLE

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

## 64. TRAIN, VALIDATION ET TEST : QUI DÉCIDE ?

Partition | Utilisation | À éviter
Train | Poids et statistiques apprises | Information issue du test
Validation | Modèle, hyperparamètres et checkpoint | Confondre sélection et estimation finale
Test | Évaluer la procédure déjà choisie | Choisir les réglages selon son score
Nouvelle distribution | Vérifier le transfert externe | La remplacer par le seul test interne

DIAPOSITIVE 64 — TRAIN, VALIDATION ET TEST : QUI DÉCIDE ?

EXPLICATION TECHNIQUE
Expliquer la séparation comme une gestion des décisions. Le train détermine les poids et, si nécessaire, les paramètres du prétraitement. La validation guide le choix de l'architecture, des hyperparamètres et du checkpoint. Le test intervient une fois le protocole de choix terminé. Il n'est pas interdit de constater qu'un score test est faible ; ce qui est problématique est de continuer à l'optimiser en prétendant conserver une estimation indépendante. Si le protocole est modifié après l'observation du test, il faut une nouvelle évaluation indépendante pour une affirmation forte.

QUESTION À POSER
Peut-on ajuster la normalisation sur l’ensemble des images ?

RÉPONSE ATTENDUE
Pas si elle apprend des statistiques : l’ajustement doit être limité au train.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 65. MÉTRIQUES ET MATRICE DE CONFUSION

DIAPOSITIVE 65 — MÉTRIQUES ET MATRICE DE CONFUSION

EXPLICATION TECHNIQUE
Pour une classe donnée, considérer cette classe comme positive et toutes les autres comme négatives. Dans la matrice de confusion des notebooks, les lignes sont les vraies classes et les colonnes les prédictions ; annoncer cette convention. Une classe rare peut avoir un rappel faible tout en contribuant peu à l'accuracy globale. Le macro-F1 moyenne les F1 calculés séparément par classe ; ce n'est pas le F1 calculé à partir d'une précision macro et d'un rappel macro. Prévoir une convention lorsque le dénominateur est nul et afficher les effectifs pour contextualiser les métriques.

ÉQUATION — SOURCE LATEX
\operatorname{precision}=\frac{TP}{TP+FP},\quad\operatorname{rappel}=\frac{TP}{TP+FN},\quad F_1=\frac{2PR}{P+R}

QUESTION À POSER
Le macro-F1 est-il le F1 de la précision et du rappel moyens ?

RÉPONSE ATTENDUE
Non : il moyenne les F1 calculés classe par classe.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 66. TRANSFERT : RÉUTILISER UNE REPRÉSENTATION

DIAPOSITIVE 66 — TRANSFERT : RÉUTILISER UNE REPRÉSENTATION

EXPLICATION TECHNIQUE
Séparer backbone et tête dans l'équation. Les poids du backbone contiennent une représentation issue d'un entraînement antérieur ; ils ne sont pas universellement pertinents. Dans le TP, la source contient les chiffres 0 à 4 et la cible les chiffres 5 à 9. Les espaces d'étiquettes sont disjoints, mais le type d'image reste proche. C'est un transfert pédagogique contrôlé, distinct d'un réseau préentraîné sur ImageNet. Le coût de préentraînement source doit être annoncé quand on compare les budgets, même s'il est partagé entre plusieurs tâches cibles.

ÉQUATION — SOURCE LATEX
f(x)=h_{\psi}(g_{\phi}(x)),\qquad\phi\leftarrow\phi_{\rm source},\quad\psi\leftarrow\psi_{\rm nouvelle}

QUESTION À POSER
Pourquoi remplacer la dernière couche ?

RÉPONSE ATTENDUE
Parce que les classes et éventuellement le nombre de sorties de la cible changent.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 67. TROIS STRATÉGIES DE TRANSFERT

Stratégie | Backbone | Tête | Usage / limite
Depuis zéro | Aléatoire, entraîné | Entraînée | Référence de comparaison
Features gelées | Source, figé | Entraînée | Peu de labels, capacité d’adaptation limitée
Fine-tuning | Source, adapté | Entraînée | Plus flexible, risque de surapprentissage

DIAPOSITIVE 67 — TROIS STRATÉGIES DE TRANSFERT

EXPLICATION TECHNIQUE
Comparer les procédures à données et partition identiques. L'extraction de caractéristiques apprend seulement la tête ; elle économise le passage arrière du backbone et limite la flexibilité. Le fine-tuning part d'un état source mais adapte une partie ou la totalité du réseau avec un taux contrôlé. L'entraînement depuis zéro fournit une référence indispensable. Un transfert peut être négatif si la représentation source ou le protocole est mal adapté. Dans le TP, le budget cible est annoncé et le coût source présenté séparément ; le test n'est pas utilisé pour décider laquelle des stratégies conserver.

QUESTION À POSER
Quelle baseline permet de détecter un transfert négatif ?

RÉPONSE ATTENDUE
Le même modèle entraîné depuis zéro avec un protocole comparable.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 68. FINE-TUNING : UNE PROCÉDURE EXPLICITE

DIAPOSITIVE 68 — FINE-TUNING : UNE PROCÉDURE EXPLICITE

EXPLICATION TECHNIQUE
Une phase de tête seule peut éviter que des gradients provenant d'une tête aléatoire perturbent immédiatement la représentation source. Après le dégel, il faut reconstruire l'optimiseur ou lui ajouter les nouveaux paramètres si ceux-ci n'étaient pas inclus. Des groupes de paramètres autorisent un taux différent pour la tête et pour le backbone. Aucune séquence de phases ne garantit un gain ; c'est une procédure à tester et à comparer. Si l'on change de domaine ou de prétraitement, vérifier aussi la distribution des activations et les statistiques des couches de normalisation.

QUESTION À POSER
Que faut-il vérifier dans l’optimiseur après un dégel ?

RÉPONSE ATTENDUE
Que les paramètres nouvellement entraînables font partie de ses groupes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 69. GEL DES POIDS ET MODE ÉVALUATION

DIAPOSITIVE 69 — GEL DES POIDS ET MODE ÉVALUATION

EXPLICATION TECHNIQUE
Ces deux commandes répondent à des questions différentes. Un backbone peut être figé du point de vue des poids tout en mettant à jour les buffers BatchNorm si son mode reste train. Inversement, eval ne bloque pas les gradients d'un paramètre qui les requiert. Dans notre petit CNN, il n'y a ni BatchNorm ni Dropout ; cela isole le mécanisme de transfert. Pour un ResNet importé, ce détail devient essentiel. Faire vérifier les drapeaux requires_grad, l'appartenance aux groupes d'optimiseur et l'évolution des buffers avant et après une époque.

QUESTION À POSER
Pourquoi un backbone sans mise à jour de poids peut-il produire des sorties différentes ?

RÉPONSE ATTENDUE
Le dropout et les statistiques de BatchNorm peuvent encore changer.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 70. UTILISER UN MODÈLE PRÉENTRAÎNÉ PUBLIC

DIAPOSITIVE 70 — UTILISER UN MODÈLE PRÉENTRAÎNÉ PUBLIC

EXPLICATION TECHNIQUE
Ce bloc est une extension de lecture, distincte du TP CPU sans téléchargement. Avec Torchvision, l'objet weights expose les transformations attendues : redimensionnement, recadrage et normalisation. Les images doivent avoir un nombre de canaux adapté, et l'ordre des classes de la tête source n'est plus valable lorsque l'on remplace celle-ci. Le téléchargement de poids nécessite un accès réseau. L'extrait ne constitue pas un entraînement complet ni une démonstration de performance. Le notebook principal montre le même mécanisme de séparation backbone-tête à partir d'un préentraînement source réalisé localement.

QUESTION À POSER
Pourquoi conserver le prétraitement associé aux poids ?

RÉPONSE ATTENDUE
La distribution d’entrée fait partie des hypothèses du préentraînement.

LECTURES ET RÉFÉRENCES
Torchvision 0.23 — ResNet18
https://docs.pytorch.org/vision/0.23/models/generated/torchvision.models.resnet18.html

## 71. COMPARER DES EXPÉRIENCES

À conserver | Pourquoi
Split et graine | Comparer sur les mêmes observations
Architecture et paramètres | Identifier la capacité entraînée
Optimiseur, pas et batch | Reproduire le budget d’apprentissage
Critère de checkpoint | Comprendre la sélection
Score, effectifs et temps | Interpréter performance et coût

DIAPOSITIVE 71 — COMPARER DES EXPÉRIENCES

EXPLICATION TECHNIQUE
Un tableau d'expériences doit permettre de reconstruire les décisions. En plus du score, conserver la graine, le découpage, la configuration, le nombre de mises à jour et le temps mesuré sur un matériel identifié. Une comparaison à une seule graine reste indicative. Les ablations changent un facteur à la fois lorsque l'objectif est d'isoler son effet ; si plusieurs facteurs changent, le résultat concerne une recette complète. Les coûts source et cible du transfert doivent être distingués. Une expérience terminée avec une précision faible peut être pédagogiquement utile si elle est documentée et correctement interprétée.

QUESTION À POSER
Peut-on attribuer un gain au dropout si l’on a aussi changé la largeur ?

RÉPONSE ATTENDUE
Non, pas sans expérience supplémentaire isolant les effets.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 72. ANALYSE D’ERREURS : REGARDER LES EXEMPLES

DIAPOSITIVE 72 — ANALYSE D’ERREURS : REGARDER LES EXEMPLES

EXPLICATION TECHNIQUE
Le score global masque des mécanismes très différents : une classe peut être sous-représentée, une annotation erronée ou un exemple simplement ambigu à faible résolution. Afficher ensemble vérité, prédiction et confiance, sans prendre cette confiance pour une probabilité calibrée. Construire une hypothèse d'erreur puis une vérification ciblée. Si l'analyse du test guide une modification du modèle, le test a servi au développement et ne doit plus être présenté comme une estimation indépendante de cette nouvelle version. Les notebooks emploient la validation pour l'investigation et réservent le test au bilan final.

QUESTION À POSER
Quel risque présente l’inspection répétée du test pour améliorer le modèle ?

RÉPONSE ATTENDUE
Le test devient progressivement un outil de sélection.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 73. TP 03 · MESURER LE TRANSFERT

DIAPOSITIVE 73 — TP 03 · MESURER LE TRANSFERT

EXPLICATION TECHNIQUE
Répartition : 25 minutes de préparation, 35 minutes d'apprentissage source, 55 minutes de comparaison des trois stratégies, 35 minutes d'analyse et 30 minutes de restitution. Les étiquettes cible sont remappées de 5–9 vers 0–4 pour la nouvelle tête à cinq sorties. Les données source et cible sont séparées par classe ; aucune image cible n'est utilisée pour apprendre la source. Chaque stratégie choisit son checkpoint sur la validation. Le test compare des procédures fixées à l'avance. Un score moins bon après transfert constitue un résultat à expliquer, pas une raison de modifier le test.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Un tableau des trois protocoles, leur coût et une interprétation du transfert positif ou négatif.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 74. JOUR 3 · À RETENIR

DIAPOSITIVE 74 — JOUR 3 · À RETENIR

EXPLICATION TECHNIQUE
Faire conclure chaque binôme avec trois phrases : quelle configuration a été comparée, quelle observation a été faite sur la validation, et quelle explication reste une hypothèse. Revenir sur la taille du domaine source et sur le nombre réduit de labels cible. Les résultats du petit jeu ne permettent pas d'affirmer qu'une famille d'architectures domine universellement. Préparer la transition : les CNN mélangent localement l'information avec des poids indépendants de l'exemple ; l'attention calculera une pondération entre éléments dépendant du contenu observé.

QUESTION À POSER
Qu’apportera l’attention par rapport à une convolution locale ?

RÉPONSE ATTENDUE
Un mélange entre positions dont les poids dépendent du contenu.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 75. ATTENTION ET TRANSFORMERS

DIAPOSITIVE 75 — ATTENTION ET TRANSFORMERS

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 76. JOUR 4 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Séquences | Représentation, récurrence et positions | 60
Attention | Q, K, V, softmax et masques | 90
Architecture | Têtes, normalisation et blocs Transformers | 90
TP 04 | Calcul d’attention et tests de causalité | 150
Synthèse | Dimensions, coût et questions de contrôle | 30

DIAPOSITIVE 76 — JOUR 4 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 77. UNE SÉQUENCE COMME TENSEUR

DIAPOSITIVE 77 — UNE SÉQUENCE COMME TENSEUR

EXPLICATION TECHNIQUE
Donner plusieurs exemples de tokens : sous-mots en texte, instants d'une série temporelle ou patches d'une image. Le vocabulaire et la tokenisation déterminent l'espace d'entrée ; des modèles avec des tokenisations différentes ne sont pas comparables directement par la seule perplexité. Les séquences peuvent avoir des longueurs variées. Le padding est une commodité de calcul, pas une observation : il doit être exclu de l'attention et, selon la tâche, de la perte. Distinguer la dimension d d'une représentation continue et la taille V du vocabulaire d'identifiants discrets.

ÉQUATION — SOURCE LATEX
X\in\mathbb R^{B\times n\times d}

QUESTION À POSER
Un token correspond-il toujours à un mot complet ?

RÉPONSE ATTENDUE
Non : il peut représenter un sous-mot, un caractère, un patch ou un autre élément.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 78. RÉCURRENCE ET DÉPENDANCES LONGUES

DIAPOSITIVE 78 — RÉCURRENCE ET DÉPENDANCES LONGUES

EXPLICATION TECHNIQUE
Cette parenthèse explique la motivation historique, sans prétendre que la récurrence est obsolète. Un RNN partage ses poids dans le temps et condense le passé dans un état. Les gradients sur de longues distances impliquent de nombreux produits de Jacobiennes. Des mécanismes comme LSTM et GRU ont été conçus pour améliorer cette dynamique. L'attention introduit un chemin direct entre positions, au prix d'un calcul potentiellement quadratique. Des architectures récurrentes ou à état restent pertinentes lorsque le coût mémoire ou la structure du flux les favorise.

ÉQUATION — SOURCE LATEX
h_t=\phi(W_xx_t+W_hh_{t-1}+b)

QUESTION À POSER
Quel compromis apparaît avec des interactions entre toutes les positions ?

RÉPONSE ATTENDUE
Un chemin plus direct, mais davantage de calcul et de mémoire selon l’implémentation.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 79. EMBEDDINGS : DES IDENTIFIANTS AUX VECTEURS

DIAPOSITIVE 79 — EMBEDDINGS : DES IDENTIFIANTS AUX VECTEURS

EXPLICATION TECHNIQUE
Une entrée entière n'est pas une grandeur ordinale : l'identifiant 8 n'est pas intrinsèquement plus proche de 9 que de 2. L'embedding transforme cet index en vecteur continu. Sa table comporte V×d paramètres, ce qui peut devenir coûteux pour un grand vocabulaire. Seules les lignes utilisées contribuent directement à une étape donnée, selon le calcul et l'optimiseur. La proximité géométrique des vecteurs est une conséquence de l'objectif appris et ne garantit pas une relation sémantique précise. Pour le mini-Transformer, les tokens sont volontairement de petits symboles entiers afin d'isoler le mécanisme.

ÉQUATION — SOURCE LATEX
E\in\mathbb R^{V\times d},\qquad x_t=E[\operatorname{id}(t),:]

QUESTION À POSER
Combien de paramètres pour V=1000 et d=64 ?

RÉPONSE ATTENDUE
64 000, sans biais.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 80. INFORMATION DE POSITION

DIAPOSITIVE 80 — INFORMATION DE POSITION

EXPLICATION TECHNIQUE
La propriété de permutation concerne une auto-attention sans masque positionnel et avec les mêmes projections à toutes les positions. Un masque causal introduit déjà une structure d'ordre, mais ne remplace pas toutes les informations de position utiles. Dans le notebook, une table de positions apprises est ajoutée à chaque embedding avant les blocs. Cela fixe une longueur maximale prévue et ne garantit pas une extrapolation à des positions jamais vues. Les encodages relatifs et rotatifs constituent d'autres choix, seulement mentionnés ici pour situer cette famille de solutions.

ÉQUATION — SOURCE LATEX
X_0=E[\text{tokens}]+P,\qquad\operatorname{SA}(\Pi X)=\Pi\operatorname{SA}(X)

QUESTION À POSER
Que signifie l’équivariance par permutation de l’auto-attention non masquée ?

RÉPONSE ATTENDUE
Permuter les tokens permute les sorties correspondantes.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 81. ENCODAGE SINUSOÏDAL DES POSITIONS

DIAPOSITIVE 81 — ENCODAGE SINUSOÏDAL DES POSITIONS

EXPLICATION TECHNIQUE
Décrire t comme la position et i comme un index de paire de caractéristiques. Les fréquences réparties sur plusieurs échelles rendent les positions distinguables dans différents régimes. Pour un décalage donné, les formules trigonométriques relient les sinus et cosinus de positions voisines par une transformation linéaire dans chaque paire. Cela motive l'approche sans prouver qu'un modèle entraîné sur une longueur donnée fonctionnera arbitrairement loin. Comparer avec la table apprise du TP : moins de structure imposée mais aucune valeur apprise au-delà des indices disponibles.

ÉQUATION — SOURCE LATEX
PE_{t,2i}=\sin\!\left(\frac{t}{10000^{2i/d}}\right),\qquad PE_{t,2i+1}=\cos\!\left(\frac{t}{10000^{2i/d}}\right)

QUESTION À POSER
L’encodage sinusoidal contient-il des paramètres entraînables ?

RÉPONSE ATTENDUE
Pas dans sa forme déterministe standard.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 82. L’ATTENTION COMME SOMME PONDÉRÉE

DIAPOSITIVE 82 — L’ATTENTION COMME SOMME PONDÉRÉE

EXPLICATION TECHNIQUE
Cette écriture suffit à expliquer le mécanisme sans métaphore obligatoire. La requête détermine ce que la position i cherche ; la clé fournit un espace de comparaison ; la valeur porte l'information mélangée dans la sortie. Les clés et les valeurs peuvent avoir des dimensions différentes, mais la dimension des requêtes doit correspondre à celle des clés pour un produit scalaire. Avec softmax, la sortie avant projection est dans l'enveloppe convexe des valeurs. Cela n'implique pas que le bloc complet soit une simple moyenne, puisqu'il comprend des projections, des résidus et des non-linéarités.

ÉQUATION — SOURCE LATEX
o_i=\sum_{j=1}^{n_k}\alpha_{ij}v_j,\qquad\sum_j\alpha_{ij}=1,\quad\alpha_{ij}\ge0

QUESTION À POSER
Sur quel axe les poids doivent-ils sommer à un ?

RÉPONSE ATTENDUE
Sur l’axe des clés consultées par chaque requête.

LECTURES ET RÉFÉRENCES
Romain Tavenard — Introduction au Deep Learning, 2025
https://rtavenar.github.io/deep_book/book_fr.pdf

## 83. Q, K, V : PROJECTIONS APPRISES

DIAPOSITIVE 83 — Q, K, V : PROJECTIONS APPRISES

EXPLICATION TECHNIQUE
Ici, X a n lignes et d colonnes, en omettant le batch. Les matrices W ont donc l'orientation entrée×sortie, contrairement à la convention de stockage de nn.Linear exposée plus tôt. Le calcul reste identique : une bibliothèque stockant sortie×entrée applique la transposée. Q et K ont n×d_k éléments, V en a n×d_v. Les trois matrices sont différentes en général, même si leur entrée est commune. Le gradient traverse à la fois les valeurs et les scores qui règlent leur mélange ; l'attention est entraînée de bout en bout.

ÉQUATION — SOURCE LATEX
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V\\W_Q,W_K\in\mathbb R^{d\times d_k},\quad W_V\in\mathbb R^{d\times d_v}

QUESTION À POSER
Q=K=V dans une auto-attention ?

RÉPONSE ATTENDUE
Pas en général : l’entrée est commune, les projections apprises sont distinctes.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 84. SCORES D’ATTENTION : TOUTES LES PAIRES

DIAPOSITIVE 84 — SCORES D’ATTENTION : TOUTES LES PAIRES

EXPLICATION TECHNIQUE
Écrire explicitement un produit scalaire entre une ligne de Q et une ligne de K. La transposition de K permet de calculer tous ces produits en une seule opération. Les lignes n'ont pas besoin d'avoir la même longueur en cross-attention : n_q peut être la longueur cible et n_k la longueur source. La largeur d_k doit en revanche être la même pour les deux. Le facteur racine carrée sera justifié ensuite. Une carte de scores brute n'est pas encore une carte de probabilités : ses valeurs peuvent être positives ou négatives et leur somme est quelconque.

ÉQUATION — SOURCE LATEX
S=\frac{QK^\top}{\sqrt{d_k}},\qquad S_{ij}=\frac{q_i^\top k_j}{\sqrt{d_k}}

QUESTION À POSER
Quelle est la forme si Q a 5 lignes et K en a 8 ?

RÉPONSE ATTENDUE
5 × 8, avec une largeur d_k commune.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 85. POURQUOI DIVISER PAR √dₖ ?

DIAPOSITIVE 85 — POURQUOI DIVISER PAR √dₖ ?

EXPLICATION TECHNIQUE
Annoncer les hypothèses : composantes centrées, indépendantes, de variance unité, avec indépendance appropriée entre q et k. Chaque produit q_r k_r a alors une variance d'ordre un et la variance de la somme est proportionnelle au nombre de termes. Les représentations réelles n'obéissent pas exactement à ces hypothèses ; il s'agit d'une justification d'échelle. Un softmax très concentré peut avoir de faibles dérivées pour de nombreuses directions. Le facteur ne normalise pas la norme exacte de chaque requête et ne transforme pas le produit scalaire en similarité cosinus.

ÉQUATION — SOURCE LATEX
\operatorname{Var}\!\left(\sum_{r=1}^{d_k}q_rk_r\right)\approx d_k\quad\Longrightarrow\quad\operatorname{Var}\!\left(\frac{q^\top k}{\sqrt{d_k}}\right)\approx1

QUESTION À POSER
Le facteur 1/√dₖ réalise-t-il une normalisation cosinus ?

RÉPONSE ATTENDUE
Non : il ne divise pas par les normes individuelles de q et k.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 86. SOFTMAX PUIS AGRÉGATION DES VALEURS

DIAPOSITIVE 86 — SOFTMAX PUIS AGRÉGATION DES VALEURS

EXPLICATION TECHNIQUE
Montrer que multiplier une matrice n_q×n_k par n_k×d_v produit n_q×d_v. Chaque requête obtient sa propre combinaison de valeurs. La même clé peut contribuer fortement à plusieurs requêtes ; il n'y a pas de contrainte de somme un par colonne. Le mécanisme n'est donc pas un appariement exclusif. Pour un batch multi-têtes, les axes batch et tête sont indépendants et le softmax reste appliqué sur le dernier axe des clés. Une erreur d'axe peut produire des tenseurs de formes plausibles tout en changeant complètement l'opération.

ÉQUATION — SOURCE LATEX
A=\operatorname{softmax}_{\rm lignes}(S),\qquad O=AV\in\mathbb R^{n_q\times d_v}

QUESTION À POSER
Les colonnes de A doivent-elles aussi sommer à un ?

RÉPONSE ATTENDUE
Non : seule chaque distribution sur les clés, donc chaque ligne, est normalisée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 87. ATTENTION : EXEMPLE NUMÉRIQUE COMPLET

DIAPOSITIVE 87 — ATTENTION : EXEMPLE NUMÉRIQUE COMPLET

EXPLICATION TECHNIQUE
Calculer les scores avant le softmax : les éléments diagonaux valent 1/racine(2) et les autres zéro. Le poids diagonal est exp(1/racine(2))/(exp(1/racine(2))+1), soit environ 0,6697615. Multiplier ensuite les poids de chaque ligne par V. La deuxième composante de la première sortie vaut deux fois 0,3302385, soit 0,660477. L'exemple volontairement petit montre que la sortie ne copie pas nécessairement un token unique. Le notebook refait le calcul en NumPy puis le compare à la version PyTorch, avec des assertions sur les valeurs et les sommes des lignes.

ÉQUATION — SOURCE LATEX
Q=K=\begin{bmatrix}1&0\\0&1\end{bmatrix},\quad V=\begin{bmatrix}1&0\\0&2\end{bmatrix}\\A\approx\begin{bmatrix}0.6698&0.3302\\0.3302&0.6698\end{bmatrix},\quad O\approx\begin{bmatrix}0.6698&0.6605\\0.3302&1.3395\end{bmatrix}

QUESTION À POSER
Pourquoi la seconde coordonnée de O₁ vaut-elle environ 0,6605 ?

RÉPONSE ATTENDUE
La seconde valeur contient 2, pondéré par environ 0,3302.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 88. MASQUE CAUSAL ET MASQUE DE PADDING

DIAPOSITIVE 88 — MASQUE CAUSAL ET MASQUE DE PADDING

EXPLICATION TECHNIQUE
Distinguer l'information temporelle interdite de l'information absente. Une ligne entièrement masquée peut produire des NaN : il faut garantir au moins une clé accessible pour chaque requête effectivement évaluée. Les requêtes correspondant au padding doivent être exclues de la perte ou de l'agrégation finale selon la tâche. Les conventions booléennes des API peuvent différer ; nn.MultiheadAttention traite True comme une interdiction pour son masque booléen, alors que certaines fonctions d'attention optimisée utilisent un sens différent. Notre code manuel emploie masked_fill avec True pour interdire explicitement.

ÉQUATION — SOURCE LATEX
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases},\qquad A=\operatorname{softmax}(S+M)

QUESTION À POSER
Multiplier les scores interdits par zéro suffit-il ?

RÉPONSE ATTENDUE
Non : exp(0) reste positif. Il faut les exclure avant la normalisation.

LECTURES ET RÉFÉRENCES
PyTorch 2.8 — MultiheadAttention
https://docs.pytorch.org/docs/2.8/generated/torch.nn.MultiheadAttention.html

## 89. MULTI-HEAD ATTENTION

DIAPOSITIVE 89 — MULTI-HEAD ATTENTION

EXPLICATION TECHNIQUE
Dans la configuration standard, d est divisible par h et chaque tête utilise d_k=d_v=d/h. La concaténation restaure d composantes, puis W_O mélange l'information provenant des têtes. Les têtes peuvent apprendre des relations différentes, mais elles peuvent aussi être redondantes ; on ne doit pas leur attribuer automatiquement une fonction linguistique précise. À largeur d constante, augmenter h n'augmente pas forcément les paramètres des grandes projections, mais modifie la dimension par tête et certains coûts intermédiaires. L'entraînement ajuste ensemble toutes les projections.

ÉQUATION — SOURCE LATEX
\operatorname{head}_r=\operatorname{Attn}(XW_Q^{(r)},XW_K^{(r)},XW_V^{(r)})\\\operatorname{MHA}(X)=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W_O

QUESTION À POSER
Pour d=256 et h=8, quelle largeur par tête ?

RÉPONSE ATTENDUE
32.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 90. DÉPLIAGE DES AXES MULTI-TÊTES

Étape | Forme standard | Exemple B=2,n=4,d=8,h=2
Projection Q/K/V | B × n × d | 2 × 4 × 8
Séparation des têtes | B × h × n × dₕ | 2 × 2 × 4 × 4
Scores | B × h × n × n | 2 × 2 × 4 × 4
Mélange des valeurs | B × h × n × dₕ | 2 × 2 × 4 × 4
Concaténation | B × n × d | 2 × 4 × 8

DIAPOSITIVE 90 — DÉPLIAGE DES AXES MULTI-TÊTES

EXPLICATION TECHNIQUE
Partir du tenseur B×n×d produit par une projection. On le reforme en B×n×h×d_h, puis on transpose les axes pour obtenir B×h×n×d_h. Le produit avec les clés transposées sur les deux derniers axes donne B×h×n×n. Après le mélange des valeurs, on inverse la permutation et on réunit les têtes. En PyTorch, un transpose peut rendre le stockage non contigu ; reshape sait parfois copier, tandis que view peut exiger contiguous. Le point conceptuel reste de ne pas fusionner des axes qui n'ont pas la même signification.

QUESTION À POSER
Pourquoi transpose-t-on avant de calculer les scores ?

RÉPONSE ATTENDUE
Pour que chaque tête calcule indépendamment ses interactions entre positions.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 91. LAYERNORM : NORMALISER CHAQUE TOKEN

DIAPOSITIVE 91 — LAYERNORM : NORMALISER CHAQUE TOKEN

EXPLICATION TECHNIQUE
Dans le Transformer étudié, chaque token est normalisé séparément sur son dernier axe. Les paramètres gamma et beta ont d composantes partagées entre positions. LayerNorm ne mélange donc pas les tokens et ne transmet pas à elle seule d'information entre positions. Elle n'utilise pas les statistiques mobiles de BatchNorm ; ce contraste explique une partie de son intérêt pour des batches et longueurs variables. La normalisation influe sur l'échelle des activations et la dynamique d'optimisation, mais n'est pas un mécanisme de masquage ni une méthode de correction des fuites de cible.

ÉQUATION — SOURCE LATEX
\mu_i=\frac1d\sum_{r=1}^{d}X_{ir},\quad\operatorname{LN}(X_i)=\gamma\odot\frac{X_i-\mu_i}{\sqrt{\sigma_i^2+\varepsilon}}+\beta

QUESTION À POSER
LayerNorm transmet-elle de l’information d’un token au suivant ?

RÉPONSE ATTENDUE
Pas lorsqu’elle ne normalise que les caractéristiques de chaque token.

LECTURES ET RÉFÉRENCES
Ba et al. — Layer Normalization, 2016
https://arxiv.org/abs/1607.06450

## 92. LE MLP POSITION PAR POSITION

DIAPOSITIVE 92 — LE MLP POSITION PAR POSITION

EXPLICATION TECHNIQUE
Le FFN n'est pas une attention supplémentaire. Il applique un MLP identique à chaque token ; l'échange d'information entre positions a lieu dans l'attention. Avec d_ff=4d et en négligeant les biais, les deux matrices du FFN contiennent 8d² paramètres. Les projections Q, K, V et O d'une auto-attention standard contiennent environ 4d² paramètres : le FFN peut donc représenter une part importante du bloc. L'activation du papier original est ReLU ; nos petits modèles utilisent GELU. Cette différence de variante doit être annoncée sans changer l'explication fondamentale.

ÉQUATION — SOURCE LATEX
\operatorname{FFN}(x)=W_2\,\phi(W_1x+b_1)+b_2,\qquad d\rightarrow d_{\rm ff}\rightarrow d

QUESTION À POSER
Quelle partie du bloc mélange directement les positions ?

RÉPONSE ATTENDUE
L’attention ; le FFN mélange les caractéristiques de chaque position.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 93. UN BLOC TRANSFORMER PRE-LN

DIAPOSITIVE 93 — UN BLOC TRANSFORMER PRE-LN

EXPLICATION TECHNIQUE
Le papier de 2017 emploie une organisation post-normalisation : normaliser après l'addition résiduelle. Cette diapositive décrit explicitement la variante pre-LN utilisée dans le mini-modèle. Elle modifie la circulation du gradient et les conditions d'optimisation. On ne doit pas présenter une variante comme la seule définition possible d'un Transformer. Les dropout éventuels sont omis de la formule pour faire ressortir les branches ; dans le code, leur place et leur taux doivent être identifiables. Les formes des deux termes additionnés doivent toujours correspondre, y compris lors de changements de largeur.

ÉQUATION — SOURCE LATEX
U=X+\operatorname{MHA}(\operatorname{LN}_1(X))\\Y=U+\operatorname{FFN}(\operatorname{LN}_2(U))

QUESTION À POSER
Où se place la normalisation dans un bloc post-LN ?

RÉPONSE ATTENDUE
Après la somme entre l’entrée résiduelle et la sortie de la sous-couche.

LECTURES ET RÉFÉRENCES
Xiong et al. — On Layer Normalization in the Transformer Architecture, 2020
https://arxiv.org/abs/2002.04745

## 94. ENCODEUR : CONTEXTUALISER UNE SÉQUENCE

DIAPOSITIVE 94 — ENCODEUR : CONTEXTUALISER UNE SÉQUENCE

EXPLICATION TECHNIQUE
Un encodeur bidirectionnel est utile lorsque toute l'entrée est disponible. Pour une classification de séquence, une représentation spéciale ou une agrégation masquée peut alimenter la tête. Pour une étiquette par token, la tête est appliquée à chaque position. Il faut traiter le padding de manière cohérente dans l'attention, l'agrégation et la perte. L'adjectif bidirectionnel n'implique pas une récurrence : il décrit l'accès aux positions à gauche et à droite. Le même bloc peut être employé avec un masque causal dans une implémentation, mais le régime d'information change alors.

ÉQUATION — SOURCE LATEX
X_L=\operatorname{Block}_L\circ\cdots\circ\operatorname{Block}_1(X_0)

QUESTION À POSER
Peut-on utiliser un encodeur non masqué pour prédire le prochain token sans fuite ?

RÉPONSE ATTENDUE
Non si les tokens futurs sont présents dans son entrée.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 95. CROSS-ATTENTION : RELIER DEUX SÉQUENCES

DIAPOSITIVE 95 — CROSS-ATTENTION : RELIER DEUX SÉQUENCES

EXPLICATION TECHNIQUE
Dans un Transformer encodeur-décodeur de traduction, l'encodeur produit une mémoire source contextualisée et le décodeur interroge cette mémoire. Les scores ont alors n cible lignes et n source colonnes. Le masque de padding source interdit les positions ajoutées, tandis que la causalité s'applique principalement à l'auto-attention de la cible. Une cross-attention n'est pas intrinsèquement une traduction : elle peut aussi relier des modalités différentes. Il faut indiquer quels tenseurs fournissent Q et lesquels fournissent K et V pour rendre l'architecture compréhensible.

ÉQUATION — SOURCE LATEX
Q=X_{\rm cible}W_Q,\quad K=H_{\rm source}W_K,\quad V=H_{\rm source}W_V

QUESTION À POSER
Quelle longueur retrouve-t-on en sortie de cross-attention ?

RÉPONSE ATTENDUE
La longueur des requêtes, donc celle de la cible ici.

LECTURES ET RÉFÉRENCES
Vaswani et al. — Attention Is All You Need, 2017
https://arxiv.org/abs/1706.03762

## 96. TROIS FAMILLES D’ARCHITECTURES

Famille | Accès aux positions | Exemple de tâche
Encodeur | Toutes les positions disponibles | Classification / étiquetage
Décodeur seul | Passé et position courante | Prédiction du prochain token
Encodeur-décodeur | Source complète + cible causale | Transformation d’une séquence en une autre

DIAPOSITIVE 96 — TROIS FAMILLES D’ARCHITECTURES

EXPLICATION TECHNIQUE
Le nom Transformer couvre plusieurs régimes de calcul. Un encodeur consulte l'entrée disponible dans les deux directions. Un décodeur seul utilise une attention causale pour modéliser une séquence auto-régressive. Un encodeur-décodeur combine une mémoire source et une génération cible avec cross-attention. Le code PyTorch d'un petit décodeur seul peut réutiliser une pile nommée TransformerEncoder avec un masque causal ; le nom de la classe ne détermine pas à lui seul le régime probabiliste. Demander de tracer l'accès à l'information plutôt que de se fier seulement aux noms des composants.

QUESTION À POSER
Un décodeur seul nécessite-t-il une cross-attention ?

RÉPONSE ATTENDUE
Non : il peut ne contenir que de l’auto-attention causale et des FFN.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 97. COÛT DE L’ATTENTION DENSE

DIAPOSITIVE 97 — COÛT DE L’ATTENTION DENSE

EXPLICATION TECHNIQUE
La matrice n×n apparaît pour chaque tête et chaque exemple lorsque l'implémentation la matérialise. Pour n=2048 et h=8, on obtient 33554432 éléments par exemple ; en float32, les seuls scores représentent 128 MiB, avant les gradients et les autres activations. Ce calcul ne constitue pas la mémoire totale d'un modèle. Des algorithmes optimisés évitent de conserver toute la matrice en mémoire tout en calculant l'attention exacte. Ils ne rendent pas automatiquement les interactions denses linéaires en calcul. Le FFN peut dominer pour certaines dimensions et longueurs.

ÉQUATION — SOURCE LATEX
T_{\rm attn}=O(n^2d),\quad T_{\rm proj+FFN}=O(nd^2)\\M_{\rm scores}=O(Bhn^2)\quad\text{si les scores sont materialises}

QUESTION À POSER
Doubler n multiplie-t-il la taille de la matrice de scores par deux ?

RÉPONSE ATTENDUE
Non : par quatre, à batch et nombre de têtes constants.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 98. ATTENTION MANUELLE : LE CŒUR DU CODE

DIAPOSITIVE 98 — ATTENTION MANUELLE : LE CŒUR DU CODE

EXPLICATION TECHNIQUE
Relier ligne par ligne l'extrait aux trois équations de l'attention. La transposition n'inverse que les deux derniers axes de K ; elle ne permute ni le batch ni la tête. Le masque doit être broadcastable vers la forme des scores. masked_fill retire les scores interdits en leur attribuant moins l'infini. Softmax est appliqué au dernier axe. L'extrait omet volontairement les projections et le dropout pour isoler le noyau du calcul ; le notebook complet les encapsule dans une classe multi-têtes et contrôle les dimensions avant l'agrégation.

QUESTION À POSER
Quelle erreur commet-on en utilisant softmax sur l’axe des requêtes ?

RÉPONSE ATTENDUE
On normalise une autre relation que la distribution des clés pour chaque requête.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 99. TP 04 · VÉRIFIER L’ATTENTION

DIAPOSITIVE 99 — TP 04 · VÉRIFIER L’ATTENTION

EXPLICATION TECHNIQUE
Déroulé : 25 minutes de calcul manuel, 45 minutes pour suivre les axes de la classe multi-têtes, 35 minutes de tests de masques, 25 minutes d'analyse des gradients et 20 minutes de restitution. Le test de causalité remplace les tokens futurs tout en gardant le préfixe identique : les sorties du préfixe doivent rester identiques en mode évaluation, avec dropout désactivé. Une carte d'attention peut illustrer une dépendance calculée, mais ne constitue pas une explication causale complète d'une décision. Les corrigés explicitent aussi le cas d'une ligne entièrement masquée.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Les valeurs numériques de référence et un test qui échouerait si le masque causal était retiré.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 100. EXERCICE · UN BLOC À 256 DIMENSIONS

DIAPOSITIVE 100 — EXERCICE · UN BLOC À 256 DIMENSIONS

EXPLICATION TECHNIQUE
La largeur de tête vaut 256/8=32. Les quatre projections d×d contiennent 4×256²=262144 paramètres. Le FFN contient 256×1024 + 1024×256 =524288 paramètres. Le total des matrices de ces sous-couches est 786432. Cette somme n'inclut pas les embeddings, la tête de sortie, les biais ni les paramètres de normalisation. Les paramètres ne dépendent pas de n pour ces matrices, mais la mémoire d'attention et les activations en dépendent. Faire expliquer pourquoi plusieurs têtes ne multiplient pas nécessairement d'autant le nombre total de paramètres lorsque d reste fixe.

QUESTION À POSER
Quelle sous-couche porte ici deux fois plus de poids matriciels ?

RÉPONSE ATTENDUE
Le FFN : 524 288 contre 262 144 pour les projections d’attention.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 101. JOUR 4 · À RETENIR

DIAPOSITIVE 101 — JOUR 4 · À RETENIR

EXPLICATION TECHNIQUE
Faire reconstruire un bloc sans regarder les diapositives : embedding plus position, normalisation, projections, scores masqués, softmax, valeurs, concaténation, projection, résidu, puis FFN et second résidu. Les détails de variante doivent être annoncés, notamment pre-LN et post-LN. Une question utile consiste à retirer un composant fictivement : sans masque causal, une prédiction de token pourrait lire sa cible ; sans information de position, une auto-attention non masquée conserve l'équivalence par permutation. La journée suivante entraînera effectivement un petit modèle causal et reliera vision et séquences avec les patches.

QUESTION À POSER
Quelle vérification relie directement le code à la causalité ?

RÉPONSE ATTENDUE
Modifier le futur et vérifier que les sorties du préfixe restent identiques.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 102. MODÈLES CAUSAUX ET SYNTHÈSE

DIAPOSITIVE 102 — MODÈLES CAUSAUX ET SYNTHÈSE

EXPLICATION TECHNIQUE
Cette journée articule les concepts et leur mise à l'épreuve. Commencer par une restitution de la séance précédente. Faire expliciter les dimensions avant toute exécution. Le déroulé représente 420 minutes de formation effective ; pauses et déjeuner sont à ajouter. Les durées des activités sont ajustables à l'intérieur de cette enveloppe. L'objectif est une compréhension justifiée par un calcul, une expérience contrôlée ou une vérification du code.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 103. JOUR 5 · DÉROULÉ DES 7 HEURES

Séquence | Travail attendu | Minutes
Modélisation | Objectif causal, génération et perplexité | 75
Vision Transformer | Patches, position et comparaison aux CNN | 60
Protocole | Ablations, limites et préparation du projet | 45
TP 05 | Mini-Transformer causal sur séquences synthétiques | 180
Évaluation | Restitution argumentée et synthèse transversale | 60

DIAPOSITIVE 103 — JOUR 5 · DÉROULÉ DES 7 HEURES

EXPLICATION TECHNIQUE
Présenter les cinq séquences de la journée. Les activités de cours incluent les questions au tableau et les démonstrations. Le travail pratique se fait en binôme mais chaque étudiant conserve un compte rendu personnel. Dans le débrief, demander une prédiction avant de montrer une sortie de code et distinguer une observation expérimentale d'une propriété mathématique. La somme des cinq durées est exactement 420 minutes. Les pauses ne sont pas comprises dans ce total.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 104. OBJECTIF AUTO-RÉGRESSIF

DIAPOSITIVE 104 — OBJECTIF AUTO-RÉGRESSIF

EXPLICATION TECHNIQUE
La factorisation par la règle de la chaîne est exacte pour toute distribution de séquence ; le choix architectural détermine comment les probabilités conditionnelles sont paramétrées. Le token de début permet de définir le premier contexte. La moyenne doit ignorer les cibles de padding quand elles ne représentent pas une observation. En entraînement, toutes les positions peuvent être calculées en parallèle grâce au masque causal, même si la génération sera séquentielle. Une séquence avec plusieurs documents concaténés exige une décision sur les frontières et l'information autorisée entre documents.

ÉQUATION — SOURCE LATEX
p_\theta(x_{1:T})=\prod_{t=1}^{T}p_\theta(x_t\mid x_{<t})\\\mathcal L=-\frac1T\sum_{t=1}^{T}\log p_\theta(x_t\mid x_{<t})

QUESTION À POSER
Pourquoi l’entraînement peut-il être parallèle alors que la génération est séquentielle ?

RÉPONSE ATTENDUE
Les vrais préfixes sont disponibles au train ; à l’inférence les prochains tokens restent à produire.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 105. DÉCALER ENTRÉES ET CIBLES

DIAPOSITIVE 105 — DÉCALER ENTRÉES ET CIBLES

EXPLICATION TECHNIQUE
Montrer une séquence très courte avec des identifiants : [BOS,2,4,EOS]. L'entrée est [BOS,2,4] et la cible [2,4,EOS]. La sortie à la position de 2 doit prédire 4 en ayant accès à BOS et 2, mais pas à 4 en entrée future. Si l'on donne la même séquence comme entrée et cible, le modèle peut apprendre à copier le token qu'il voit déjà. Ce bug peut produire une perte très faible et une génération inutile. Le test de causalité et la lecture du décalage sont donc complémentaires.

ÉQUATION — SOURCE LATEX
\text{inputs}=s_{0:T-1},\qquad\text{targets}=s_{1:T}

QUESTION À POSER
Une perte quasi nulle dès le départ peut-elle révéler un mauvais décalage ?

RÉPONSE ATTENDUE
Oui : le modèle peut voir directement le token qu’on lui demande de prédire.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 106. TEACHER FORCING ET GÉNÉRATION

DIAPOSITIVE 106 — TEACHER FORCING ET GÉNÉRATION

EXPLICATION TECHNIQUE
Ce contraste est souvent appelé différence d'exposition aux contextes. La vraisemblance reste un objectif bien défini, mais une bonne performance conditionnée par les vrais préfixes ne garantit pas une génération de longue durée sans dérive. Dans le TP, on évalue séparément la perte sur séquences tenues à part et la capacité de continuation après un préfixe fixé. Les séquences sont synthétiques pour rendre la règle attendue explicite. Les modèles de langage réels ajoutent des contraintes de données, de tokenisation et d'usage qui ne sont pas reproduites par ce petit laboratoire.

QUESTION À POSER
Pourquoi vérifier aussi des continuations libres ?

RÉPONSE ATTENDUE
Pour observer le comportement lorsque le modèle conditionne sur ses propres sorties.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 107. DÉCODAGE : ARGMAX, TEMPÉRATURE ET ÉCHANTILLONNAGE

DIAPOSITIVE 107 — DÉCODAGE : ARGMAX, TEMPÉRATURE ET ÉCHANTILLONNAGE

EXPLICATION TECHNIQUE
Une petite température concentre la masse vers les plus grands logits ; une grande température aplatit la distribution. La limite vers zéro approche une sélection des maxima, mais diviser effectivement par zéro est une erreur. Top-k garde un nombre fixe de candidats ; top-p conserve un ensemble dont la masse cumulée atteint un seuil selon la règle employée. Ces transformations changent la distribution de génération et ne corrigent pas une connaissance erronée. Dans le TP, commencer par un décodage glouton pour comprendre le mécanisme, puis varier la température avec une graine de tirage explicite.

ÉQUATION — SOURCE LATEX
p_\tau(x_t=k\mid x_{<t})=\operatorname{softmax}(z/\tau)_k,\qquad\tau>0

QUESTION À POSER
Une température plus faible garantit-elle une réponse correcte ?

RÉPONSE ATTENDUE
Non : elle concentre la distribution du modèle, y compris sur ses erreurs.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 108. PERPLEXITÉ ET NORMALISATION DE LA PERTE

DIAPOSITIVE 108 — PERPLEXITÉ ET NORMALISATION DE LA PERTE

EXPLICATION TECHNIQUE
V désigne ici l'ensemble des positions valides, et non la taille du vocabulaire utilisée précédemment ; le préciser oralement. Pour éviter l'ambiguïté, parler de positions évaluées. Une distribution uniforme sur dix tokens a une perplexité de dix lorsque ces dix tokens sont les cibles possibles. Une perplexité de un correspond à une probabilité un sur les cibles observées dans cette évaluation, limite idéale. La perplexité d'un modèle à caractères et celle d'un modèle à sous-mots n'ont pas la même unité de normalisation. Dans le TP, les premiers symboles aléatoires restent intrinsèquement difficiles à prédire.

ÉQUATION — SOURCE LATEX
\operatorname{PPL}=\exp\!\left(-\frac1M\sum_{t\in\mathcal V}\log p_\theta(x_t\mid x_{<t})\right),\quad M=|\mathcal V|

QUESTION À POSER
Que vaut exp(log(8)) ?

RÉPONSE ATTENDUE
8 ; c’est la perplexité d’un choix uniforme parmi huit possibilités.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 109. CACHE K/V À L’INFÉRENCE

DIAPOSITIVE 109 — CACHE K/V À L’INFÉRENCE

EXPLICATION TECHNIQUE
Dans une multi-head attention standard, la largeur totale des clés et celle des valeurs valent souvent d, donc d_KV=d. Des variantes à clés et valeurs partagées changent ce facteur. Le cache contient un tenseur K et un tenseur V par couche, batch et position. Pour chaque nouveau token, on ne recalcule pas les projections du passé, mais on doit toujours comparer sa requête aux clés conservées. La mémoire croît donc avec la longueur de contexte. Le mini-modèle du TP recalcule volontairement le préfixe complet pour rester lisible ; il n'implémente pas de cache.

ÉQUATION — SOURCE LATEX
M_{KV}\approx2BLnd_{KV}\times\text{octets par element}

QUESTION À POSER
Le cache supprime-t-il le besoin de consulter les tokens passés ?

RÉPONSE ATTENDUE
Non : il réutilise leurs clés et valeurs déjà calculées.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 110. VISION TRANSFORMER : UNE IMAGE EN PATCHES

DIAPOSITIVE 110 — VISION TRANSFORMER : UNE IMAGE EN PATCHES

EXPLICATION TECHNIQUE
La formule suppose H et W divisibles par P et des patches carrés de côté P. Chaque patch est converti en vecteur, puis en embedding appris. Un token de classification peut être ajouté ; d'autres variantes utilisent une agrégation des sorties. La couche de projection peut être implémentée comme une convolution de noyau P et de stride P, ce qui relie les deux familles sans les rendre identiques. Les positions sont indispensables pour préserver l'organisation spatiale dans l'approche standard. Une réduction de P augmente fortement le nombre de tokens et le coût de l'attention.

ÉQUATION — SOURCE LATEX
n=\frac{HW}{P^2},\qquad x_i\in\mathbb R^{P^2C},\qquad z_i=x_iW_E+p_i

QUESTION À POSER
Combien de valeurs dans un patch RGB 16×16 ?

RÉPONSE ATTENDUE
16×16×3 = 768.

LECTURES ET RÉFÉRENCES
Dosovitskiy et al. — An Image is Worth 16x16 Words, 2020
https://arxiv.org/abs/2010.11929

## 111. PATCHES : CALCULER LE COÛT

DIAPOSITIVE 111 — PATCHES : CALCULER LE COÛT

EXPLICATION TECHNIQUE
Le dernier rapport porte uniquement sur les matrices d'attention des tokens visuels sans token de classification. En ajoutant ce token, le rapport exact devient 785²/197², légèrement différent de seize. Cette précision montre l'intérêt de distinguer une approximation d'ordre de grandeur d'un calcul exact. La projection de chaque patch change aussi avec P ; tout le coût du modèle ne suit donc pas nécessairement le même facteur. Des patches plus petits gardent une granularité spatiale plus fine, mais le compromis dépend de la tâche, des données et du budget.

ÉQUATION — SOURCE LATEX
\left(\frac{224}{16}\right)^2=196,\qquad\left(\frac{224}{8}\right)^2=784\\\frac{784^2}{196^2}=16

QUESTION À POSER
Diviser la taille de patch par deux double-t-il n ?

RÉPONSE ATTENDUE
Non : n est multiplié par quatre pour une image 2D.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 112. CNN ET VIT : COMPARER LES HYPOTHÈSES

Aspect | CNN standard | ViT standard
Interaction initiale | Locale, noyaux partagés | Patches puis attention globale
Position | Structure de grille dans les opérations | Encodage explicite des positions
Résolution | Champ réceptif progressif | Nombre de patches / tokens
Coût typique | Dépend des cartes et des noyaux | Attention dense quadratique en tokens
Conclusion | À valider pour la tâche | À valider pour la tâche

DIAPOSITIVE 112 — CNN ET VIT : COMPARER LES HYPOTHÈSES

EXPLICATION TECHNIQUE
Éviter un classement absolu des architectures. Les CNN imposent une localité et un partage spatiaux forts ; les Transformers permettent un mélange global dépendant du contenu dans les couches d'attention denses. Les données, le préentraînement, les augmentations, la résolution et le budget peuvent modifier les conclusions empiriques. Un ViT ne devient pas automatiquement supérieur parce qu'il appartient à une famille plus récente. Les architectures hybrides et hiérarchiques rendent la frontière moins stricte. L'évaluation doit comparer des recettes documentées plutôt qu'un nom de famille isolé.

QUESTION À POSER
Quel contrôle est indispensable pour comparer CNN et ViT ?

RÉPONSE ATTENDUE
Le protocole de données, préentraînement, résolution et budget de calcul.

LECTURES ET RÉFÉRENCES
Dosovitskiy et al. — An Image is Worth 16x16 Words, 2020
https://arxiv.org/abs/2010.11929

## 113. TRANSFERT DANS UN TRANSFORMER

DIAPOSITIVE 113 — TRANSFERT DANS UN TRANSFORMER

EXPLICATION TECHNIQUE
Le même principe backbone-tête vu pour les CNN s'applique aux encodeurs Transformers, mais avec des choix supplémentaires : tokenisation, positions, masque et agrégation. Pour un modèle causal, la tâche peut être formulée comme une prédiction de séquence ; il faut vérifier que les cibles et le masquage de perte correspondent à l'objectif. Les méthodes d'adaptation à faible nombre de paramètres sont une extension possible, pas détaillée dans ce cours d'introduction. Un petit nombre de paramètres adaptés ne garantit ni un faible coût d'inférence ni une absence d'oubli sur la tâche source.

QUESTION À POSER
Changer seulement la tête suffit-il si la tokenisation est incompatible ?

RÉPONSE ATTENDUE
Non : les identifiants, embeddings et prétraitements doivent rester cohérents.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 114. LIMITES ET INTERPRÉTATION

DIAPOSITIVE 114 — LIMITES ET INTERPRÉTATION

EXPLICATION TECHNIQUE
Les informations peuvent transiter par plusieurs têtes, les valeurs, les résidus et les MLP ; une carte d'attention ne décrit donc qu'une partie du calcul. Une vérification causale demanderait des interventions contrôlées, elles-mêmes à interpréter prudemment. Pour les modèles génératifs, la vraisemblance entraîne la prédiction de séquences, pas une garantie de vérité. Dans un projet appliqué, analyser les populations concernées, la provenance et l'autorisation d'usage des données, ainsi que les risques d'erreurs spécifiques au domaine. Les exemples jouets du cours ne valident pas ces conditions de déploiement.

QUESTION À POSER
Une carte d’attention suffit-elle à prouver pourquoi une classe a été prédite ?

RÉPONSE ATTENDUE
Non : elle ne couvre qu’une partie des chemins de calcul.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 115. TP 05 : LA TÂCHE ET SON PROTOCOLE

DIAPOSITIVE 115 — TP 05 : LA TÂCHE ET SON PROTOCOLE

EXPLICATION TECHNIQUE
Les quatre premiers symboles sont choisis dans un alphabet de huit possibilités. Ils ne peuvent pas tous être déduits du préfixe ; une partie de la perte est donc irréductible pour cette distribution. Les répétitions suivantes constituent les positions de copie prévisibles. Le découpage se fait sur les motifs de quatre symboles, avant la répétition, pour éviter qu'une séquence identique soit présente dans plusieurs partitions. Il s'agit d'une tâche synthétique de structure séquentielle, pas d'une évaluation linguistique. La métrique de copie complète la perplexité et permet de distinguer apprentissage de la règle et prédiction des symboles initiaux.

ÉQUATION — SOURCE LATEX
\langle BOS\rangle,\ a,b,c,d,\ a,b,c,d,\ a,b,c,d,\ \langle EOS\rangle

QUESTION À POSER
Pourquoi ne pas exiger une perte globale nulle ?

RÉPONSE ATTENDUE
Les symboles initiaux du motif sont aléatoires et ne sont pas entièrement prévisibles.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 116. TP 05 · ENTRAÎNER UN MINI-TRANSFORMER

DIAPOSITIVE 116 — TP 05 · ENTRAÎNER UN MINI-TRANSFORMER

EXPLICATION TECHNIQUE
Organisation : 25 minutes pour les données et l'objectif, 40 minutes d'inspection du bloc et des masques, 40 minutes d'entraînement et d'évaluation, 40 minutes d'ablation et 35 minutes de restitution. Les étudiants doivent d'abord prouver l'absence d'accès au futur. Le test modifie la fin d'une entrée et vérifie les logits du préfixe. L'ablation choisit un facteur, par exemple la position ou le nombre de têtes, puis reconduit le même protocole. Un modèle qui apprend imparfaitement la copie reste utile pour étudier le diagnostic. Le notebook inclut aussi un exercice de mise en patches sans entraînement d'un grand ViT.

QUESTION À POSER
Que doit contenir un résultat interprétable ?

RÉPONSE ATTENDUE
Une expérience reproductible et une explication des mécanismes, même si la copie reste imparfaite.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 117. ABLATIONS : CHANGER UN FACTEUR

Modification | Hypothèse à tester | Contrôle requis
Sans position | Effet de l’information d’ordre | Même données et budget
Une seule tête | Diversité des projections | Largeur totale fixée
Plus de couches | Capacité / optimisation | Coût et normes des gradients
Sans masque causal | Détection de fuite | Test de préfixe doit échouer

DIAPOSITIVE 117 — ABLATIONS : CHANGER UN FACTEUR

EXPLICATION TECHNIQUE
Faire annoncer l'hypothèse avant l'exécution. Une ablation utile doit préciser ce qui reste fixé et ce qui change. Retirer le masque causal est un contrôle de fuite, pas une amélioration admissible de l'objectif auto-régressif. Retirer les positions teste un mécanisme différent et peut ne pas dégrader toutes les tâches de la même manière. Modifier les têtes à largeur fixe ne modifie pas nécessairement les paramètres comme le ferait une modification de d. Les conclusions doivent citer le nombre de graines et le budget réellement exécuté, et distinguer une observation locale d'une propriété générale.

QUESTION À POSER
Si un modèle sans masque obtient une meilleure perte, peut-on le déclarer meilleur en génération causale ?

RÉPONSE ATTENDUE
Non : il peut exploiter les tokens futurs et résoudre un autre problème.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 118. ÉVALUATION FINALE : EXPLIQUER ET PROUVER

Critère | Preuve | Points
Compréhension mathématique | Dérivation et dimensions | 5
Implémentation | Calcul vérifié et masques corrects | 5
Protocole expérimental | Séparation et sélection sans fuite | 5
Analyse et limites | Erreurs, ablation et discussion | 5

DIAPOSITIVE 118 — ÉVALUATION FINALE : EXPLIQUER ET PROUVER

EXPLICATION TECHNIQUE
Le barème proposé totalise vingt points et peut être adapté au règlement de la formation. Évaluer une présentation de dix minutes par binôme, accompagnée d'un notebook exécuté et d'un court compte rendu individuel. Faire poser une question de gradient, une question de formes et une question de validité expérimentale. Ne pas attribuer tous les points à l'accuracy : un résultat performant avec fuite de données échoue sur le protocole. Inversement, un résultat limité mais bien contrôlé peut démontrer la maîtrise des mécanismes et une capacité de diagnostic.

QUESTION À POSER
Quelle preuve doit accompagner un score ?

RÉPONSE ATTENDUE
Le protocole qui permet de comprendre ce que ce score estime.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 119. SYNTHÈSE : UN MÊME CADRE, PLUSIEURS STRUCTURES

DIAPOSITIVE 119 — SYNTHÈSE : UN MÊME CADRE, PLUSIEURS STRUCTURES

EXPLICATION TECHNIQUE
Revenir à l'unité conceptuelle du cours. Un MLP, un CNN et un Transformer diffèrent par leurs opérations et les contraintes qu'ils imposent, mais chacun définit une fonction paramétrée et une perte différentiable. La rétropropagation traverse le graphe correspondant ; l'optimiseur utilise ses gradients. Les paramètres de convolution sont partagés entre positions spatiales, ceux du FFN Transformer entre tokens, et les poids d'attention eux-mêmes sont calculés à partir du contenu. La performance dépend ensuite des données et de l'évaluation, pas uniquement de la famille du modèle.

ÉQUATION — SOURCE LATEX
\text{donnees}\ \longrightarrow\ f_\theta\ \longrightarrow\ \mathcal L\ \xrightarrow{\rm backprop}\ \nabla_\theta\mathcal L\ \xrightarrow{\rm optimiseur}\ \theta'

QUESTION À POSER
Qu’est-ce qui change entre MLP, CNN et Transformer ?

RÉPONSE ATTENDUE
Le graphe de calcul et ses hypothèses de structure, tout en gardant le cadre d’apprentissage.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 120. EXERCICE DE SYNTHÈSE : AUDIT D’UN MODÈLE

DIAPOSITIVE 120 — EXERCICE DE SYNTHÈSE : AUDIT D’UN MODÈLE

EXPLICATION TECHNIQUE
Corrigé : les cibles doivent être décalées d'un token par rapport aux entrées. Sinon, la position courante voit déjà le symbole à prédire. Un masque additif constitué de zéros et de uns n'interdit aucune position ; il décale seulement les scores. Le masque doit utiliser moins l'infini pour les positions interdites, ou une convention booléenne correctement interprétée par l'API. Tester un petit exemple explicite de décalage et modifier les tokens futurs tout en comparant les logits du préfixe en mode évaluation. Vérifier également les sommes des poids et les entrées de la matrice masquée.

QUESTION À POSER
Quels deux contrôles doit-on exécuter avant de relancer l’entraînement ?

RÉPONSE ATTENDUE
Un exemple entrée/cible décalé et un test d’invariance du préfixe aux modifications du futur.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 121. LECTURES FOURNIES : FONDEMENTS ET MÉTHODE

DIAPOSITIVE 121 — LECTURES FOURNIES : FONDEMENTS ET MÉTHODE

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

## 122. ARTICLES : ARCHITECTURES ET OPTIMISATION

DIAPOSITIVE 122 — ARTICLES : ARCHITECTURES ET OPTIMISATION

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

## 123. NORMALISATION ET DOCUMENTATION DES API

DIAPOSITIVE 123 — NORMALISATION ET DOCUMENTATION DES API

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

## 124. VOTRE CHECKLIST TECHNIQUE

DIAPOSITIVE 124 — VOTRE CHECKLIST TECHNIQUE

EXPLICATION TECHNIQUE
Terminer par un retour sur les preuves de maîtrise annoncées en début de cours. Demander à chaque étudiant de choisir la compétence la moins solide et de formuler un exercice permettant de la renforcer. Les notebooks, les sources LaTeX et les notes du présentateur permettent de reprendre les démonstrations. Le meilleur prolongement consiste à garder un protocole simple et à augmenter progressivement la difficulté, plutôt qu'à passer directement à un modèle très grand. Une compréhension précise des formes, des objectifs et des masques se transfère à des architectures plus complexes.

QUESTION À POSER
Quelle partie savez-vous vérifier sans vous fier seulement à un score ?

RÉPONSE ATTENDUE
Les dimensions, le gradient, les invariants de l’attention et la séparation des données.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX

## 125. MERCI

DIAPOSITIVE 125 — MERCI

EXPLICATION TECHNIQUE
Inviter les étudiants à revenir sur une équation, un résultat de TP ou une erreur observée. Pour chaque question, partir du problème et des hypothèses avant de choisir une architecture. La conclusion attendue est une capacité à expliquer un calcul, à construire une expérience et à reconnaître les limites de ce que les résultats démontrent. Les suites possibles sont un projet de vision sur données réelles, une étude de modèles préentraînés ou une analyse plus avancée de l'optimisation et des architectures séquentielles.

EXEMPLE ET EXPLICATION PÉDAGOGIQUES ORIGINAUX
