# orchestrate docker containers


## docker_image module

builds docker images

## docker_servie module

commande pour docker-compose

## docker-container module

Permet de lancer des containers.
Peut-être un peu bas niveau si on veut mettre des containers en relation (network).


## ansible container module

Passe par un ficher .yml descriptif docker-compose-like.
On gagne une abstraction sur la plateforme qui supporte docker (kubernetes, openshift...).
Pas forcément pertinent puisque le marché part sur kubernetes.
Il vaut peut-être mieux investir sur des fichiers descriptifs kubernetes.
