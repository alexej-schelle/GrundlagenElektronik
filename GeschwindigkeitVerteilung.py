###############################################################################################################################################
#                                                                                                                                             #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                             #
###############################################################################################################################################

# Grundlegendes Anwendungsbeispiel für die Modellierung mithilfe von Monte-Carlo Simulationen (mit direkten Realisierungen)

import random
import math
import matplotlib as plt
import matplotlib.pyplot as plt
import operator

n_total = 100000 # Variable für Anzahl der Monte-Carlo Iterationen

VarVelocityPerpendicular = [] # Array zur Speicherung von Geschwindkeiten
VarWaveLength = [] # Array zur Speicherung von Wellenlaengen

Voltage = 1.0 # Volts in units of Volts
VarEnergy = 1.602176634E-19*Voltage # In Units of Joule (U = 1.0 Volts)

StartEnergy = VarEnergy

Temperature = 200.0 # In Units of Kelvin
ThermalEnergy = 1.5*1.38064852E-23*Temperature # In Units of Joule  

ElektronenMasse = 9.10938356E-31 

for i in range(0, n_total):

    Voltage = random.gauss(1.0, math.sqrt(1.0)) # Generiere Zufallszahl m mit Gleichverteilung
    VarEnergy = 1.602176634E-19*math.fabs(Voltage)

    if (operator.gt(min((math.exp(StartEnergy/ThermalEnergy))/(math.exp(VarEnergy/ThermalEnergy)),1.00),random.uniform(0.00,1.00))):

        VarVelocityPerpendicular.append(math.sqrt(math.fabs(2.0*VarEnergy/ElektronenMasse))/1000.0)
        VarWaveLength.append(math.sqrt(math.fabs(math.pi/(VarEnergy/ElektronenMasse*1.0E9))))

        StartEnergy = VarEnergy
        
plt.figure(1)
plt.hist(VarVelocityPerpendicular, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$v~[10^3~Meter~pro~Sekunde]$', fontsize = 14)
plt.ylabel('$p$', fontsize = 14)
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/FigureGeschwindigkeit.png')

plt.figure(2)
plt.hist(VarWaveLength, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$\lambda~[nm]$', fontsize = 14)
plt.ylabel('$p$', fontsize = 14)
plt.xlim([0.0, 1.0E-8])
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/FigureWellenlaenge.png')