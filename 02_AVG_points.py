# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 11:28:08 2023

@author: jerem
"""
import pandas as pd
import statistics
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Lire le fichier Excel en utilisant la première colonne comme index
df = pd.read_excel('02_database.xlsx', index_col=0)

# Créer un dictionnaire pour stocker les moyennes par année
moyennes_par_annee = {}

# Parcourir les années de 1990 à 2022 inclusivement
for annee in range(1990, 2024):
    valeurs_annee = df.loc[annee].tolist()
    
    # Retirer les valeurs nulles de la liste et obtenir les 10 plus hautes valeurs
    valeurs_annee = [i for i in valeurs_annee if i != 0]
    valeurs_annee = sorted(valeurs_annee, reverse=True)
    valeurs_annee = valeurs_annee[:10]
    
    # Calcul de la moyenne pour l'année en cours
    moyenne_annee = round(statistics.mean(valeurs_annee), 2)
    
    # Stocker la moyenne dans le dictionnaire moyennes_par_annee avec l'année comme clé
    moyennes_par_annee[annee] = moyenne_annee

# Créer une figure et un axe pour le graphique
fig, ax = plt.subplots()

# Initialiser le graphique avec les valeurs de la première année
annees = []
moyennes = [] #line1
mean= [] #line2

line1, = ax.plot([], [], color='b', marker='o')
line2, = ax.plot ([],[],label='Average of dataset', color='r')
titre = ax.set_title('NBA TOP 10 scorer average points')

#Création d'une fonction init et update nécessaires à l'animation

def init():
    ax.set_xlim(1990, 2023)
    ax.set_ylim(min(moyennes_par_annee.values()) - 15, max(moyennes_par_annee.values()) + 15)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average points')
    ax.legend()
    return line1,line2, titre

def update(frame):
    annee = 1990 + frame
    annees.append(annee)
    moyennes.append(moyennes_par_annee[annee])
    mean=sum(moyennes)/len(moyennes)
    line1.set_data(annees, moyennes)
    line2.set_data(annees,mean)
    titre.set_text(f'NBA TOP 10 scorer average points : {moyennes_par_annee[annee]} points - {annee}')
    return line1,line2, titre

fig.set_figheight(6)
fig.set_figwidth(10)

# Créer l'animation
ani = FuncAnimation(fig, update, frames=range(0, 34), init_func=init, blit=True)

# Sauvegarder l'animation en tant que gif
ani.save('NBA TOP 10 scorer average points.GIF', writer='pillow')

# Afficher l'animation
plt.show()
