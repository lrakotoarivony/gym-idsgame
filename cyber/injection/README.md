# Injection de fichier

## Requirements

Cette partie nécessite la librairie python exiftool.

## Explication

Cette attaque modélise le cas où l'attaquant crée un fichier php qu'il va uploader sur le serveur du défenseur pour avoir accès au password. Pour des raisons de simplicité l'upload n'est pas vraiment réalisé et le script php n'est pas interprété.  
Le défenseur va juste regarder le nom du fichier ainsi que ses métadonnées afin de déterminer si le fichier uploadé est malicieux ou non. Dans cette simulation, le serveur d'upload a pour vocation de récupérer des images et non des scripts.  

## Défense

Le défenseur a trois niveaux de puissance. Il va utiliser la fonction defend_injection pour déterminer si le fichier uploadé est malicieux ou non.  

* Au niveau 0 : Le défenseur vérifie si le fichier finit bien avec une extension correspondant à une image  
* Au niveau 1 : Le défenseur vérifie que le nom de fichier contient seulement une extension  
* Au niveau 2 : Le défenseur vérifie que le MIME Type du fichier correspond bien à une image  

## Attaque

L'attaque a trois niveaux de puissance. Il va utiliser la fonction attack_injection pour uploader un fichier php avec une payload.  

* Au niveau 0 : L'attaquant upload un fichier avec une extension php  
* Au niveau 1 : L'attaquant upload un fichier avec une double extension  
* Au niveau 2 : L'attaquanr upload un fichier avec une double extension et un null byte  

## Comparaison attaque-défense  

Pourcentage de réussite de l'attaque en fonction des niveaux d'attaque et de défense
| Défense / Attaque      |   0     |  1     |   2    |
|---    |:-:    |:-:    |--:    |
|  0     |  0     |  100     |  100     |
|   1    |  0     |  0     |  100     |
|    2   |  0     |  0     |  0     |

Temps d'exécution moyen d'une attaque en fonction des niveaux d'attaque et de défense en secondes
| Défense / Attaque      |   0     |  1     |   2    |
|---    |:-:    |:-:    |--:    |
|  0     |  0.00     |  0.00     |  0.00     |
|   1    |  0.00     |  0.00     |  0.00     |
|    2   |  0.00     |  0.00     |  0.13     |
