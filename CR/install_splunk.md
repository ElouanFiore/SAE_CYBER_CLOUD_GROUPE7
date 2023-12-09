# Installation de splunk

## installation du serveur

L'installation du serveur d'écoute est très simple c'est un packet .deb, il est donc déployabale avec 
```bash
sudo dpkg -i splunk_entreprise.deb
```

il écoute sur le port 8000 et demanderas lors de son installation un mot de passe qui sera utilisée pour la connection à l'interface web.

on peut alors d'y connecter avec:
127.0.0.1, localhost ou elastic.sevenkingdoms.local
```url
elastic.sevenkingdoms.local:8000
```

## déploiement des agents.

j'ai commencé par rajouter les éléments qu'il faudrait télécharger dans le playbook de goad ([goad-dc](../playbooks/goad-dc.yaml) et [goad-srv](../playbooks/goad-srv.yaml))
j'ai donc automatiser la copie avec la syntaxe j2 puis j'ai exécuté les différents éléments:


1. l'installation de winrar<br> ![installtion de winrar](./screen_splunk/install_winrar.png)

2. l'exécution de l'installer msi
    1. ![installateur msi](./screen_splunk/install_msi.png)
    2. la sélection des crédentiels ![passwords](./screen_splunk/credentiak.png)
    3. le paramétrage des port de destination ainsi que l'ip du serveur splunk (le même que le serveur elastic)
    ![paramétrage deployement](./screen_splunk/deployement.png)
    ![paramétrage indexeur](./screen_splunk/indexer.png)
    4. l'installation du l'agent ![agent install](./screen_splunk/installing.png)

3. le dépaquetage de l'addon windows avec winrar dans le réportoire de l'agent (c:\Program Files\Splunk Forwarder\etc\apps) ![dépaquetage du tgz](./screen_splunk/extract_addon.png)

4. la copie du fichier c:\Program Files\Splunk Forwarder\etc\apps\SplunkTAwindows\default\input.conf
dans un répertoire nouvellement créé c:\Program Files\Splunk Forwarder\etc\apps\SplunkTAwindows\local
![input.conf modifié](./screen_splunk/copy_local.png)

5. la modification du fichier inputs.conf ainsi copié (activation des sondes)
![input.conf file](./screen_splunk/modify_input.png)

6. le redémarrage du service afin de prendre en compte le nouveau fichier de configuration:
![reboot splunk forwarder](./screen_splunk/restart.png)

## Résultats

on obtient alors les agents qui remontent des données pour chacun des hôtes:

![hôtes webgui](./screen_splunk/added-1.png)