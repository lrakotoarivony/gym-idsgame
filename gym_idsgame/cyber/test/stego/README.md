# Stéganographie

## Requirements

Cette partie nécessite d'installier les librairies python import stepic, exiftool et piexif

## Explication

Cette attaque modélise le cas où le défenseur stocke dans une image de type PNG (nécessaire car pas de compression) une chaîne de caractère de type flag={password} où password correspond au mot de passe à obtenir.  
Pour cacher cette chaîne de caractère on définit trois méthodes :  
* insertion de texte : on insère le texte à la fin de l'image
* écriture dans les métadonnées : on insère le flag dans les métadonnées de l'image
* utilisation de stepic : on utilise la librairie stepic pour cacher le texte dans l'image

## Défense

La défense est statique (ce qui signifie que peu importe les cas le défenseur va agir de la même manière). On utilise la fonction defend_stega qui va à partir de l'image source cacher à l'aide d'une des trois méthodes précédentes le flag dans l'image destination.  

## Attaque

L'attaque aest statique, cela signifie que peu importe le niveau de puissance l'attaquant choisira seulement une méthode parmi les 3 pour trouver le flag. Ce choix a été fait afin de rendre la simulation plus équilibrée.

## Comparaison attaque-défense  

Pourcentage de réussite de l'attaque en fonction des niveaux d'attaque et de défense
| Défense / Attaque      |   0     |  1     |   2    |
|---    |:-:    |:-:    |--:    |
|  0     |  33     |  33     |  33     |
|   1    |  33     |  33     |  33     |
|    2   |  33     |  33     |  33     |

Temps d'exécution moyen d'une attaque en fonction des niveaux d'attaque et de défense en secondes
| Défense / Attaque      |   0     |  1     |   2    |
|---    |:-:    |:-:    |--:    |
|  0     |  0.07     |  0.07     |  0.07     |
|   1    |  0.07     |  0.07     |  0.07     |
|    2   |  0.07     |  0.07     |  0.07     |
