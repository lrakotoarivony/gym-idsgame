# Password

## Explication

Cette attaque modélise le cas où le défenseur va générer un mot de passe sécurisé et l'attaquant va essayer de bruteforcer ce mot de passe

## Défense

Le défenseur a trois niveaux de puissance. Il va utiliser la fonction defend_password pour générer un mdp sécurisé.  

* Au niveau 1 : Le défenseur génère un mdp de 4 caractère composé de lettres et de chiffre
* Au niveau 2 : Le défenseur génère un mdp de 4 caractère composé de lettres, de caractères spéciaux et de chiffre
* Au niveau 3 : Le défenseur génère un mdp de 6 caractère composé de lettres, de caractères spéciaux et de chiffre

## Attaque

L'attaque a trois niveaux de puissance. Il va utiliser la fonction attack_password pour tenter de bruteforce le mdp

* Au niveau 1 : L'attaquant bruteforce en utilisant des chaines de caractères de taille 4 avec des lettres minuscules et des chiffres
* Au niveau 2 : L'attaquant bruteforce en utilisant des chaines de caractères de taille 4 avec des lettres, des chiffres et les caractères spéciaux
* Au niveau 3 : L'attaquant bruteforce en utilisant des chaines de caractères de taille 4 avec des lettres, des chiffres et les caractères spéciaux ainsi qu'une wordlist
