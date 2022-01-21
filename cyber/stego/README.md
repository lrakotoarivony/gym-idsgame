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

L'attaque a trois niveaux de puissance. Plus son niveau est élevé, plus elle pourra choisir de méthodes disponibles pour retrouver le flag dans l'image destination.
