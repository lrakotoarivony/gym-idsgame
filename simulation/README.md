# Experiment `Cybersecurity` v0

Cela est une expérimentation de l'environnement `idsgame-cyber-v0`.  
Cet environnement est dédié à des simulations à 1 ou 2 agents ou des entrainements de RL.

La configuration de l'environnement est la suivante:  

- `num_layers=2` (number of layers between the start and end nodes)
- `num_servers_per_layer=3`
- `num_attack_types=4`
- `max_value=3`  
- `connected_layers = True`

Les attaques types sont les suivantes (cf dossier cyber pour plus d'infos) [attaque par injection de fichier, déchiffrage d'un hash, attaque sur mdp, détection de stégano dans une image]

<p align="center">
<img src="docs/env.png" width="700">
</p>

L'environnement de départ est initialisé de manière définie (introduire de l'aléatoire dans le placement des vulnérabilités n'est pas souhaitable car les attaques ne sont pas transposables).  

- `defense_val=1`
- `attack_val=0`
- `num_vulnerabilities_per_node=1`  
- `det_val=2`
- `vulnerability_val=0`
- `num_vulnerabilities_per_layer=2` 

l'environnement a des rewards discrètes (+1,-1 en fonction de la fin de chaque épisode).

## Environment 

- Env: `idsgame-cyber-v0`

## Algorithm

- Tabular Q-learning ou DQN
 
## Commands

Le script permettant l'entrainement est le script training.py

Voici un exemple d'utilisation ainsi que ses arguments

```
python training.py --num_episodes 100 --checkpoint_freq 10 --dqn --attacker_only
```

Ce script contient plusieurs arguments:  

- num_episodes : nombres d'epoch d'entrainements
- checkpoint_freq :  la fréquence de sauvegarde et d'évaluation
- dqn : si dqn ou tabular learning
- attacker_only : seulement entrainement de l'attaquant
- defender_only : seulement entrainement du défenseur  

## Analyse et test  

Cette simulation diffère de la simulation originale sur plusieurs points. Tout d'abord, contrairement à la version originelle chaque attaque possède des probabilités de succès différentes (voir dossier cyber dans l'env gym-idsgame). Cela a pour effet d'introduire de l'aléatoire et ainsi de créer des stratégies complexe qui dépendent des choix des algorithmes.   
Une version antérieure des attaques par stéganographie avait pour résultat que l'attaquant pouvait en augmentant au maximum son niveau d'attaque sur l'attaque de stégano de passer à 100%. Cela représente une stratégie gagnante et les modèles d'attaquant que j'entrainais dans cette situation tendait vers cette stratégie. Cela démontre que les algorithmes réussisent à trouver une stratégie gagnante si elle est simple. Cependant, dans ce cas, le défenseur faisait des actions randoms car peu importe ses mouvements cela menaient à une défaite. La simulation fut donc changé pour rendre cela plus réaliste.  

Un travail a également été fait sur l'environnement afin que cela soit équilibré pour l'attaquant et le défenseur. Nous allons introduire une metric nommé la hack probability qui utilise le fichier simulation.py pour réaliser 100 simulations et la hack probability représente le pourcentage de victoire de l'attaquant. On comprend aisément que le but de l'attaquant est de maximiser cette métric et inversement pour le défenseur.  
L'environnement a donc été testé via des modifications et actuellement en opposant l'attaque Attack Maximal Value (AMV) et la défense Defend Minimal Value (DMV), on obtient une hack probability de 0.55.  

### Méthodes par apprentissage vs méthodes définies:  

Dans un premier temps, nous souhaitons démontrer que les méthodes par apprentissage peuvent facilement dans cette simulation, obtenir de meilleures performances que des méthodes définies comme AMV ou DMV. Pour cela, nous avons entrainé 2 modèles de tabular q learning (présent dans le dossier modèle sous le nom d'attacker_only_new_env.npy (respectivement defender_only_new_env.npy)) sur 20001 épisodes face à DMV (respectivement AMV). Nous avons ensuite calculé la hack probability de ces confrontations.  

On obtient donc en résultat:  
- AMV vs DMV : 0.55
- Tabular Q Learning vs DMV : 0.63
- AMV vs Tabular Q Learning : 0.53

Cela démontre que les méthodes par apprentissage obtiennent de meilleurs résultats. En effet, cela s'explique car les méthodes AMV et DMV sont très pertinente dans la simulation de base car chaque attaque se comporte de la même manière. Dans notre simulation, où les attaques sont différentes il est par exemple inutile d'investir des ressources dans les attaques par stéganographie (comportement statique avec toujours 33% de chance de passer peu importe les niveaux.  

### Comparaison des méthodes d'apprentissage:  

(TO DO)
