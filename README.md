# SAE CYBER CLOUD GROUPE 7

## Synthèses

### Organisation
Nous nous sommes divisé les tâches selon ce que nous préférions faire. Nous avons d'abord déployé un GOAD sur virtualbox en attendant de pouvoir le faire sur proxmox. Nous avons aussi fait une PoC de l'automatisation de l'installation pour qu'une fois que le proxmox est disponible on ai juste nos script ansible à lancer.

#### Lucas
- Deployment GOAD Proxmox
- Scripts Python Suricata

#### Antoine
- 

#### Elouan
- open-wec
- wazuh

### Nos blocages

#### Lucas
- Attribuition de domain child sur les machines windows via Ansible (aprés j'ai reussi)

#### Antoine
- 

#### Elouan
- Génération d'un SPN pour open-wec
- 

### Ce qu'on a appris

#### Lucas
- Perfection sur l'utilisation de firewall (régles NAT, VPN, VLANs)
- Logs suricata IPS
- Utilisation d'users avec token sur proxmox
- Bonne connaissance sur infrastructures virtualisés (schematisation, deployment)

#### Antoine
- 

#### Elouan
- L'utilisation d'un AD (domaine enfant, relation entre forêt, GPO)
- Utilisattion des rôles ansible
- Perfection de git 


## Annexes
- [x] GOAD Proxmox (CR/GOAD_Proxmox.pdf)(Manuel)
- [x] [Accès VPN](CR/vpn.md) (Automatisé)
- [ ] Suricata (Manuel)
- [x] [Sysmon](CR/sysmon.md) (Automatisé)
- [x] [Audit](CR/audit.md) (Automatisé)
- [x] [open-wec](CR/openwec.md) (Automatisé)
	- [x] [WEF](CR/wef.md) (Automatisé)
- [x] [Wazuh](CR/wazuh.md) (Automatisé)
	- [x] [Installation agent par groupe DC/Servers](CR/wazuh-agent.md) (Automatisé)
- [ ] Elastic (Automatisé)
	- [ ] Elastic Agent (Automatisé)
- [ ] Splunk (Manuel)
- [x] [Versioning Git](CR/git.md)
- [ ] Attaques (Manuel)
	- [ ] Rapport
