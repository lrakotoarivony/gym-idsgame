# Password

## Explication

Cette attaque modélise le cas où le défenseur va générer un mot de passe sécurisé et l'attaquant va essayer de bruteforcer ce mot de passe

## Défense

Le défenseur a trois niveaux de puissance. Il va utiliser la fonction defend_password pour générer un mdp sécurisé.  

* Au niveau 0 : Le défenseur génère un mdp de 4 caractère composé de lettres et de chiffre
* Au niveau 1 : Le défenseur génère un mdp de 4 caractère composé de lettres, de caractères spéciaux et de chiffre
* Au niveau 2 : Le défenseur génère un mdp de 6 caractère composé de lettres, de caractères spéciaux et de chiffre

## Attaque

L'attaque a trois niveaux de puissance. Il va utiliser la fonction attack_password pour tenter de bruteforce le mdp

* Au niveau 0 : L'attaquant bruteforce en utilisant des chaines de caractères de taille 4 avec des lettres minuscules et des chiffres
* Au niveau 1 : L'attaquant bruteforce en utilisant des chaines de caractères de taille 4 avec des lettres, des chiffres et les caractères spéciaux
* Au niveau 2 : L'attaquant bruteforce en utilisant des chaines de caractères de taille 4 avec des lettres, des chiffres et les caractères spéciaux ainsi qu'une wordlist

## Comparaison attaque-défense  

Pourcentage de réussite de l'attaque en fonction des niveaux d'attaque et de défense
| Défense / Attaque      |   0     |  1     |   2    |
|---    |:-:    |:-:    |--:    |
|  0     |  12     |  12     |  13     |
|   1    |  1     |  2     |  6     |
|    2   |  0     |  0     |  0     |

Temps d'exécution moyen d'une attaque en fonction des niveaux d'attaque et de défense en secondes
| Défense / Attaque      |   0     |  1     |   2    |
|---    |:-:    |:-:    |--:    |
|  0     |  0.22     |  0.32     |  0.90     |
|   1    |  0.22     |  0.35     |  0.88     |
|    2   |  0.21     |  0.34     |  0.88     |
