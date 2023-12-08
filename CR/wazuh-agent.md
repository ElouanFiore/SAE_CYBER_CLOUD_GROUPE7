# Installation des agents Wazuh

L'installation des agents est elle aussi automatisée par un [playbook](../roles/wazuh-agent/tasks/main.yml). Grâce aux [group_vars](../group_vars/winserv/wazuh.yml) d'ansible, les agents rentrent automatiquement dans le bon groupe d'agent Wazuh.

## Limitations
Pour des raisons de connexions il était plus simple de copier l'installateur de l'agent depuis le controller ansible plutôt que d'aller le chercher à chaque fois sur internet. Mais il serait mieux d'aller le chercher sur internet pour avoir la dernière version à chaque fois. Une solution serait de mettre à jour la version de l'installateur sur le controller via le playbook avant de lancer les autres tâches.