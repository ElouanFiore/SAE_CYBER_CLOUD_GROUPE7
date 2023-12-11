# SAE CYBER CLOUD GROUPE 7

## Synthèse

### Organisation
Nous nous sommes divisé les tâches selon ce que nous préférions faire. Nous avons d'abord déployé un GOAD sur virtualbox en attendant de pouvoir le faire sur proxmox. Nous avons aussi fait une PoC de l'automatisation de l'installation pour qu'une fois que le proxmox est disponible on ai juste nos script ansible à lancer.

#### Lucas
- Deployment GOAD Proxmox
- Scripts Python Suricata
- schema réseau
- Firewall (pfsense)

#### Antoine
- Déploiement automatisé d'élastic search avec ansible (policies, agent, kibana, elastic, fleet)
- Déploiement de splunk
- Attaque de GOAD
- Déploiement du trello (création et liste des tâches)

#### Elouan
- open-wec
- wazuh
- Débug GOAD sur proxmox
- Analyse log Chainsaw/Hayabusa
- Gestion du repo git 

### Nos blocages

#### Lucas
- Attribuition de domain child sur les machines windows via Ansible (aprés j'ai reussi)

#### Antoine
- Intéraction avec les divers composants lors de l'automatisation (kibana, elastic, fleet)
- délpoiement de splunk et des spécificités des inputs
- Techniques d'énumération d'AD
- Familiaristion avec les modules windows d'ansible

#### Elouan
- Génération d'un SPN pour open-wec
- SID dupliqué des VM cloné

### Ce qu'on a appris

#### Lucas
- Perfection sur l'utilisation de firewall (régles NAT, VPN, VLANs)
- Logs suricata IPS
- Utilisation d'users avec token sur proxmox
- Bonne connaissance sur infrastructures virtualisés (schematisation, deployment)

#### Antoine
- utilisation des roles ansible
- utilisation plus en profondeur de la syntaxe jinja2 (ouverture de fichier, boucles)
- Compréehiension de l'environnement active directory et de ses enjeux (kerberos, TGT, GPO)
- l'utilisation des patch et de git.
- Les intéractions avec l'api elastic, kibana et fleet

#### Elouan
- Mise en place des forêts AD (domaine enfant, relation entre forêt, Admin du domain/d'entreprise)
- Utilisattion des rôles ansible
- Perfection de git

## Annexes
- [x] [GOAD Proxmox](CR/goad_proxmox.pdf)(Manuel)
- [x] [Accès VPN](CR/vpn.md) (Automatisé)
- [x] [Suricata (Manuel)](CR/install_suricata.md)
- [x] [Sysmon](CR/sysmon.md) (Automatisé)
- [x] [Audit](CR/audit.md) (Automatisé)
- [x] [open-wec](CR/openwec.md) (Automatisé)
	- [x] [WEF](CR/wef.md) (Automatisé)
- [x] [Wazuh](CR/wazuh.md) (Automatisé)
	- [x] [Installation agent par groupe DC/Servers](CR/wazuh-agent.md) (Automatisé)
- [x] [Elastic (Automatisé)](CR/deploiement_elastic.md)
- [x] [Splunk (Manuel)](CR/install_splunk.md)
- [x] [Versioning Git](CR/git.md)
- [x] [Attaques](CR/Pentest_GOAD.md) (Manuel)
- [x] [Chainsaw/Hayabusa](CR/log-analyze.md)
