import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Chemin vers votre fichier eve.json
chemin_fichier = '/var/log/suricata/eve.json'

# Charger le fichier JSON ligne par ligne dans une liste
with open(chemin_fichier, 'r') as fichier:
	lignes = fichier.readlines()

# Convertir chaque ligne JSON en objet Python
data = [json.loads(ligne) for ligne in lignes]

# Créer une liste de DataFrames pour chaque événement
dfs = [pd.json_normalize(event) for event in data]

# Concaténer les DataFrames en un seul DataFrame
df = pd.concat(dfs, ignore_index=True)

# Sélectionner les colonnes importantes
columns_of_interest = ['timestamp', 'src_ip', 'dest_ip', 'event_type']
df_filtered = df[columns_of_interest]

# Formater les horodatages
df_filtered['timestamp'] = pd.to_datetime(df_filtered['timestamp'])

# Filtrer les événements non vides (supprimer les lignes avec des valeurs manquantes)
df_filtered = df_filtered.dropna()

# Afficher un graphique de ligne avec seaborn
plt.figure(figsize=(12, 6))
sns.scatterplot(x='timestamp', y='src_ip', data=df_filtered)
plt.title('Graphique en ligne entre timestamp et source_ip')
plt.xlabel('Timestamp')
plt.ylabel('Source IP')
plt.xticks(rotation=45)
plt.show()
