
################################################################################################################################################
#                                                                                                                                              #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                              #
################################################################################################################################################

import os
import sys
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt

import random
import pandas
import csv

i = j = k = 0

num_cols = 1 # Definiere die Anzahl der Spalten
num_rows = 50000 # Definiere die Anzahl der Zeilen

fieldnames = ['Widerstandswert'] # Definiere den Spaltennamen als Vektor mit einer Spalte
data_field = [0.0]*num_cols # Definiere das Datenfeld

Temperature = 10.1 # Temperature in Einheiten von Kelvin
ThermalEnergy = Temperature # In Units of Joule / k_B (Boltzmann Konstante) 

Voltage = 15.0 # Wert für die Spannung

MeanR = 0.0 # Mittelwert für den Widerstand
VarianceR = 0.0 # Variable für Varianz-Definition

alpha = 1.0E2 # In Einheiten von Ohm pro Kelvin

R0 = 100.0 # In Einheiten von Ohm
T0 = 0.0

with open('import_file.csv', 'w') as f: # Adressenpfad für File Pfad
    
    writer = csv.writer(f) # Ins CSV File schreiben 
    writer.writerow(fieldnames) # In den Header des CSV Files schreiben 
    
    for i in range(0, num_rows):

        for j in range(0, num_cols):

            data_field[j] = float(random.uniform(0.0, 1000.0)) # Schreibe in den Header des CSV Files
            
        writer.writerow(data_field) # Schreibe die Daten des CSV Files 
        
df = pandas.read_csv('import_file.csv') # Einlesen der Daten aus dem CSV File - setze den korrekten Pfad mit pwd

for i in range(0, num_rows): # Berechnung der Mittelwerte und Varianzen aus den Daten
    
    MeanR = MeanR + df['Widerstandswert'][i]/num_rows # Berechnung Mittelwert aus den Daten

print(' ')
print('Der Mittelwert fuer den Widerstand lautet: ', MeanR, 'Ohm') # Ausgabe eines Mittelwerts auf dem Bildschirm

for i in range(0, num_rows): # Berechnung der Varianzen aus den Daten
    
    VarianceR = VarianceR + (df['Widerstandswert'][i] - MeanR)**2/num_rows**2 # Ausgabe eines Werts für die Varianz auf dem Bildschirm

print(' ')
print('Die Varianz fuer den Widerstand lautet: ', math.sqrt(VarianceR), 'Ohm') # Ausgabe eines Werts für die Varianz auf dem Bildschirm

MeanI = Voltage/MeanR

print(' ')

print('Der Mittelwert fuer den Strom lautet: ', math.sqrt(MeanI), '') # Ausgabe eines Werts für die Varianz auf dem Bildschirm

print(' ')

GaussStrom = []
GaussWiderstand = []
GaussEnergieStrom = []

VerteilungThermischerWiderstand = []

for i in range(0, num_rows): # Berechnung der Varianz für die Variable Strom aus den Daten
     
    GaussStrom.append(random.gauss(MeanI, Voltage/VarianceR))

for i in range(0, num_rows): # Berechnung der Varianz für die Variable Strom aus den Daten
     
    GaussWiderstand.append(random.gauss(MeanR, VarianceR))

for i in range(0, num_rows): # Berechnung der Varianz für die Variable Strom aus den Daten
     
    GaussEnergieStrom.append(random.gauss(1.5*ThermalEnergy**2, math.sqrt(ThermalEnergy)))

for i in range(0, num_rows): # Berechnung der Varianz für die Variable Strom aus den Daten
     
    VerteilungThermischerWiderstand.append(R0*(1.0 + alpha*(Temperature-T0)*random.gauss(alpha, math.sqrt(alpha))))

plt.figure(1)
plt.hist(GaussStrom, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$I~[Hz]$', fontsize = 14)
plt.ylabel('$Wahrscheinlichkeit~p$', fontsize = 14)
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/FigureStromverteilung.png')   

plt.figure(2)
plt.hist(GaussWiderstand, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$R~[Hz]$', fontsize = 14)
plt.ylabel('$Wahrscheinlichkeit~p$', fontsize = 14)
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/FigureWiderstand.png')  

plt.figure(3)
plt.hist(GaussEnergieStrom, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$E~[k_B]$', fontsize = 14)
plt.ylabel('$Wahrscheinlichkeit~p$', fontsize = 14)
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/FigureEnergie.png')

plt.figure(4)
plt.hist(VerteilungThermischerWiderstand, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$Temperatur~T$', fontsize = 14)
plt.ylabel('$Widerstand~R~[Ohm]$', fontsize = 14)
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/FigureThermischerWiderstand.png')
