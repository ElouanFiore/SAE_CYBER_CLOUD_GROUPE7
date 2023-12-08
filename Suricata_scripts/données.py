#Script our afficher les données sur eve.json
import pandas as pd
import json

# Chemin vers notre fichier eve.json
chemin_fichier = '/var/log/suricata/eve.json'

# Ligne pour Charger le fichier JSON ligne par ligne dans une liste
with open(chemin_fichier, 'r') as fichier:
    lignes = fichier.readlines()

# Ligne pour Convertir chaque ligne JSON en objet Python
data = [json.loads(ligne) for ligne in lignes]

# Ligne pour Créer une liste de DataFrames pour chaque événement
dfs = [pd.json_normalize(event) for event in data]

# Ligne pour Concaténer les DataFrames en un seul DataFrame
df = pd.concat(dfs, ignore_index=True)

# Afficher les lignes du DataFrame
print(df.iloc[0:35])
