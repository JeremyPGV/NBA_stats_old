# -*- coding: utf-8 -*-
"""
EN : 
    
    Work with data of the NBA championship. First step : collect all the 
    TOP 10 scorer from 1990 to 2023. Second step : collect the total number of 
    points scored each season between 1990-2023. Third step : get a full dataset
    in an Excel file. Fourth step : Apply the following code.
    
FR : 
    Travailler avec les données du championnat NBA. Première étape : 
    collecter tous les TOP 10 des buteurs de 1990 à 2023.
    Deuxième étape : collecte du nombre total de points marqués par un joueur 
    pour chaque saison entre 1990-2023. Troisième étape : obtenir un ensemble 
    de données complet dans un fichier Excel. 
    Quatrième étape : appliquer le code suivant.
    
"""
from sjvisualizer import DataHandler,Canvas,BarRace,StaticImage 

import json


EXCEL_FILE="01_test.xlsx"
FPS=60
DURATION=0.5

# load the data into a data frame
df = DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=FPS*DURATION*60).df

# creating the canvas
canvas = Canvas.canvas()
  
# adding the racing bar chart
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas)
canvas.add_sub_plot(bar_chart)
  
# adding a title
canvas.add_title("TOP 10 NBA SCORER", color=(0,0,0))
canvas.add_sub_title("1990 - 2023", color=(150,150,150))
  
# adding a time
canvas.add_time(df=df, time_indicator="year")

# adding a static image
ex = StaticImage.static_image(canvas=canvas.canvas, file="nba_logo.png", x_pos = 550, y_pos=25, width=125, height=125)
ex2= StaticImage.static_image(canvas=canvas.canvas, file="image.jpg", x_pos = 1300, y_pos=25, width=125, height=125)
canvas.add_sub_plot(ex)
canvas.add_sub_plot(ex2)
  

# play the animation
canvas.play(fps=FPS)


 
