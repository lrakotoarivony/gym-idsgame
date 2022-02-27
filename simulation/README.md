# Experiment `Cybersecurity` v0

Cela est une expérimentation de l'environnement `idsgame-cyber-v0`.  
Cet environnement est dédié à des simulations à 1 ou 2 agents ou des entrainements de RL.

La configuration de l'environnement est la suivante:  

- `num_layers=2` (number of layers between the start and end nodes)
- `num_servers_per_layer=3`
- `num_attack_types=4`
- `max_value=3`  
- `connected_layers = True`

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


