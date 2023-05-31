import matplotlib.pyplot as plt
import pandas as pd

# Importation des bibliothèques nécessaires

# Lecture du fichier CSV et création du DataFrame
df = pd.read_csv('Census_2016_2021.csv', index_col=0)

# Filtrage pour obtenir uniquement les données des municipalités
df_villes = df[df['Type'] == 'MÉ'].reset_index(drop=True)

# Calcul du nombre de municipalités
nombre_ME = df_villes.shape[0]
print(f"Le nombre de municipalités est de {nombre_ME}")

# Calcul de la population moyenne en 2016 et 2021
moy_16 = df_villes['Pop16'].mean()
moy_21 = df_villes['Pop21'].mean()

print(f"La population moyenne en 2016 était de {moy_16}")
print(f"La population moyenne en 2021 était de {moy_21}")
# Calcul du pourcentage d'accroissement des populations entre 2016 et 2021
df_villes['PctAcc'] = 100 * (df_villes['Pop21'] - df_villes['Pop16']) / df_villes['Pop16']

# Création de la nouvelle colonne 'Catégories' en fonction de la population
df_villes['Catégories'] = df_villes.apply(lambda row: 1 if row['Pop21'] < 2000
                                           else 2 if 2000 <= row['Pop21'] <= 9999
                                           else 3 if 10000 <= row['Pop21'] <= 24999
                                           else 4 if 25000 <= row['Pop21'] <= 99999
                                           else 5 if row['Pop21'] >= 100000
                                           else None, axis=1)
# Tracé du diagramme en barres horizontales du nombre de municipalités dans chaque catégorie
plt.subplot(2, 1, 2)
df_villes.groupby('Catégories')['Catégories'].count().plot(kind='barh', y='Index', x='Catégories')
plt.xlabel('Nombre de municipalités')
plt.ylabel('Catégories')

# Tracé du nuage de points
plt.subplot(2, 1, 1)
plt.scatter(df_villes['Pop21'], df_villes['PctAcc'])
plt.ylabel("Accroissement de la population de 2016 à 2021 [%]")
plt.xlabel("Population en 2021")

# Affichage des graphiques
plt.show()