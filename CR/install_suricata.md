# Installation du Suricata

## déploiment avec elastic et infrastructure


### Sur le serveur elastic
Suricata étant un IDS il doit donc analyser la totalité du trafic arrivant sur notre infrastructure. Nous l'installerons alors directement sur l'hôte proxmox et non sur une VM. POur se faire nous installerons un agent élatic sur l'hôte (à la main). On créera alors une policy propre à l'hôte qui assureras l'intégration de suricata (qui seras d'ailleurs la seule de la policy).


### Sur l'hôte
sur l'hôte on instancieras alors un conteneur docker avec la commande suivante:

```bash
docker run -rm -d -it --net=host --cap-add=net_admin --cap_add=net_raw --cap-add=sys_nice -v /var/log/suricata:/var/log/suricata jasonish/suricata:latest -i enp4s0
```
- run permettant de lancer une image
- -rm permettant de la détruire en cas de stop
- it pour intéragir avec
- --net=host pour se placer dans le même network que l'hôte
- --cap-add pour permetre au conteneur suricata d'intéragir avec les api kernels nécessaires
- -v permettant de monter le volume /var/log/suricata sur le répertoire /var/log/suricata du conteneur
- jasonish/suricata:latest est l'image du conteneur que nous allons déployer ici suricata
- -i enp4s0 permet de passer au conteneur l'interface enp4s0

### Intégration

Afin de l'intégration il faudra mettre en place le volume qui renseigne les logs afin que le elastic puis les passer à kibana ainsi que la police de l'hôte.
malheureusement pour une raison inconue ces logs ne remontent pas dans kibana.
