# ZeCrypt
 Programme de chiffrement basé sur Python, disponible en 4 versions.

---

## Installation
 L'installation se fait via Git, en entrant la commande suivante :   
 `git clone https://github.com/ZeMonsiM/ZeCrypt.git`

 Si vous souhaitez utiliser la version avec interface utilisateur utilisant Kivy (disponible dans le dossier GUI_V2/), vous devrez aussi installer la dépendance en exécutant :  
 `pip install kivy` (ou `pip3 install kivy` sur Linux)

---

## Version de base
 La version de base contient le coeur du programme de chiffrement ZeCrypt. Il fonctionne via le terminal de commandes et demande à l'utilisateur de fournir les informations nécessaires au chiffrement, tel que le nom du fichier en entrée, le nom du fichier en sortie et la clé de chiffrement.

 L'utilisateur peut aussi choisir de sélectionner un fichier clé au lieu d'entrer manuellement une clé choisie. Pour cela, il suffit de renseigner l'argument `file` quand le programme demande la clé. Un quatrième argument (le chemin de la clé) sera demandé et le chiffrement pourra commencer.

 De plus, le programme permet de suivre l'avancée du chiffrement via une barre de chargement.

 _Note : Le programme est extrêmement lent à chiffrer les fichiers lourds, comme les vidéos par exemple. Ce problème existe car Python est un langage interprété et lent par rapport à d'autres langages de plus bas niveau. Il est donc déconseillé de chiffrer des fichiers "lourds" (au dessus de 25Mo)._

---

## Chiffrement de masse
 Une version spéciale de ZeCrypt a été crée pour le chiffrement automatisé de centaines de fichiers. Cette version utilise multiprocessing pour optimiser le temps de chiffrement en utilisant davantage le processeur, ce qui aide quand les fichiers qu'on souhaite chiffrer pèsent au total plusieurs centaines de Mo.

 Cette version est plus difficile à utiliser, car contrairement à la version de base où les arguments sont renseignés pendant l'exécution, les arguments doivent ici être passés par la ligne de commande en exécutant le script. La syntaxe de la commande est la suivante :  
 `zecrypt_mass.py [méthode] [répertoire] [clé de chiffrement / "file"] [fichier clé (facultatif)]`  
 * Le premier argument demande si on souhaite chiffrer ou déchiffrer le fichier en entrée (argument qui devient nécessaire pour déterminer automatiquement le fichier en sortie). Le chiffrement correspond à l'option "1" et le déchiffrement à l'option "2".
 * Le second argument correspond au dossier contenant les fichiers à chiffrer.
 * Le troisième argument accepte une clé de chiffrement ou le mot clé "file" pour utiliser un fichier clé généré aléatoirement.
 * Le quatrième argument est uniquement nécessaire si le mot clé "file" est spécifié en troisième argument. Il s'agit du chemin vers le fichier clé.
 
 Les tests ont été effectués sur un dossier contenant 230 images ayant une taille totale de 450Mo environ, sur une machine utilisant un Intel Core i5 9400F. Il a fallu moins de 10 minutes pour déchiffrer le dossier, alors qu'un chiffrement de masse __sans multiprocessing__ aurait demandé plus de 10 heures sur la même machine.

---

## ZeCrypt GUI V1
 Cette version utilise tkinter pour utiliser ZeCrypt via une fenêtre graphique sur Windows. Il s'agit d'une version très rudimentaire, avec les deux options pour chiffrer et déchiffrer un fichier, ainsi qu'un bouton pour quitter le programme. Cette version, contrairement aux autres, ne permet pas d'utiliser un fichier clé et il n'y a pas d'indicateur de progression qui s'affiche. Il est déconseillé d'utiliser la version GUI V1 pour des fichiers de plusieurs Mo, la fenêtre affichant "ne répond pas" pendant le chiffrement de fichiers lourds.

 ZeCrypt GUI V1 est plus une version simple d'utilisation pour le chiffrement de fichiers de petite taille et pour ceux qui n'ont pas besoin du niveau de sécurité qu'offre un fichier clé.

 _Note : Cette version est "abandonnée" et ne verra probablement pas de mises à jours ou de corrections de bugs, il est conseillé de se diriger vers la version 2._

---

## ZeCrypt GUI V2
 La version 2 utilise Kivy pour gérer l'interface utilisateur. Cette version a été prévue pour un usage sous Android, mais je n'ai pas réussi à compiler le code pour en créer un fichier en .apk.  
 Cette version est déjà plus esthétique et utilise un thème sombre. Il suffit d'entrer le chemin du fichier à traiter dans le premier champ, la clé ou le chemin du fichier clé dans le deuxième et de cliquer sur le bouton approprié, suivant si l'utilisateur souhaite chiffrer ou déchiffrer le fichier. Pour passer d'une clé au chemin d'un fichier clé, l'utilisateur doit activer l'option "utiliser un fichier clé".

 Contrairement à la version 1, la progression s'affiche dans le texte du bas et Windows ne considère pas que le programme a planté durant le chiffrement.

---

## ZeCrypt XOR
 La version XOR du programme ZeCrypt a été ajouté pour avoir un chiffrement plus rapide des fichiers. Cette version utilise un fichier clé pour sécuriser les fichiers, que l'utilisateur peut générer avec le script `keygen.py`.
 Bien que la clé utilisée peut être identique entre les différentes versions de ZeCrypt, cet algorithme ne donne pas le même fichier en sortie ! **Les fichiers chiffrés avec la version XOR ne peuvent pas être déchiffrés avec la version classique !**

---

## Générer un fichier clé aléatoire
 Le script `keygen.py` permet à l'utilisateur de générer, via le terminal, une clé de chiffrement aléatoire de longueur donnée. Il est très simple d'utilisation et demande les informations pendant l'exécution afin de sauvegarder la clé dans un fichier `.key`.

---

## Tests de vitesse
 Des tests de vitesse seront bientôt réalisés pour donner un ordre d'idée de la différence de vitesse entre les versions de ZeCrypt.
 Le test sera réalisé sur un environnement Linux, avec un processeur Intel Core i9-13900H et 16Go de RAM. Les programmes testés sont : `zecrypt_mass.py`, `zecrypt_xor_mass.py` et `zecrypt_xor.py` (sans utiliser le multiprocessing).