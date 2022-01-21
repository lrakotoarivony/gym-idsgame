# Cryptanalyse

## Requirements

Cette partie nécessite l'installation de John the Ripper (une installation Kali Linux est préférable) et la librairie python hashlib.

## Explication

Cette attaque modélise le cas où le défenseur stocke dans un fichier texte le hash d'un password donné. Pour des mesures de simplicité, on suppose que les mdp proviennent du fichier short_ech.txt qui est un extrait de rockyou.txt.  
Pour l'instant seul les méthodes de chiffrement md5 et sha-256 sont implémentés.

## Défense

Le défenseur a trois niveaux de puissance. Il va utiliser la fonction defend_hash pour cacher un mdp chiffré dans le fichier outfile.  

* Au niveau 1 : Le défenseur choisit un chiffrement et chiffre le mdp
* Au niveau 2 : Le défenseur va modifier le mdp avec la méthode Jumbo et ensuite le chiffrer
* Au niveau 3 : Le défenseur va modifier le mdp avec la méthode Jumbo amélioré et ensuite le chiffrer

## Attaque

L'attaque a trois niveaux de puissance. Il va utiliser la fonction attack_hash avec une wordlist pour essayer de déchiffrer le mdp.  

* Au niveau 1 : L'attaquant choisit de manière aléatoire une méthode de chiffrement pour essayer de déchiffrer le mdp
* Au niveau 2 : L'attaquant utilise un hash identifier pour savoir quelle méthode de chiffrement utiliser
* Au niveau 3 : L'attaquanr utilise un hash identifier ainsi que la rule Jumbo pour déchiffrer
