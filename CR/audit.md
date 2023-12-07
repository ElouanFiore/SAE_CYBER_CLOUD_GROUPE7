# Audit

## Initialisation
Les règles d'audit ont été faite en suivant [le guide de l'anssi](https://cyber.gouv.fr/publications/recommandations-de-securite-relatives-active-directory). Eles sont configuré par un [playbook ansible](../playbooks/audit.yml) via un module communautaire.
```bash
ansible-playbook playbooks/audit.yml
```

## Limitations
Évidemment ce n'est pas une solution viable, dans un environnement AD avec beaucoup de serveurs on préférera une GPO qui se répliquera automatiquement au lieu d'un playbook long à faire tourner sur des dizaines de serveurs. Ici ça a été utile car ça a évité le clicodrome de l'utilitaire Group Policy Management a chaque réinstallation de GOAD.