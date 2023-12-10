# Analyse des logs avec Chainsaw et Hayabusa

## Conversion du xml en evtx
J'ai pu convertir les logs avec [xml2evtx](https://github.com/JPCERTCC/xml2evtx) :
![Alt text](images/analyse-evtx.png)

## Analyse avec chainsaw
L'analyse avec les sigma rules de bases de chainsaw n'a rien donnée :
![Alt text](images/analyse-chainsaw.png)

## Analyse avec hayabusa

J'ai d'abord commencé par mettre à jour les règles de détections d'hayabusa :
![Alt text](images/analyse-uphaya.png)

On peut déjà faire une liste des événements les plus récurrents :
![Alt text](images/analyse-eid.png)

Mais le plus intéressant est l'analyse des tentatives connexions échouées, on remarque qu'elles viennent toutes de l'ordinateur d'Antoine (192.168.10.200) : 
![Alt text](images/analyse-failed.png)