# WEF

## Initialisation
Les agents WEF ne sont pas initialisés avec une GPO mais directement en ajoutant les bonnes clés de registres via un [playbook ansible](../playbooks/wef.yml). Il ajoute aussi l'utilisateur 'NETWORK SERVICE' au groupe 'Event Log Readers'
```bash
ansible-playbook playbooks/wef.yml
```

## Limitations
Évidemment ce n'est pas une solution viable, dans un environnement AD avec beaucoup de serveurs on préférera une GPO qui se répliquera automatiquement au lieu d'un playbook long à faire tourner sur des dizaines de serveurs. Ici ça a été utile car ça a évité le clicodrome de l'utilitaire Group Policy Management a chaque réinstallation de GOAD.
