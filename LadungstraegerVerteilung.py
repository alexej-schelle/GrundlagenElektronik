###############################################################################################################################################
#                                                                                                                                             #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                             #
###############################################################################################################################################

# Grundlegendes Anwendungsbeispiel für die Modellierung mithilfe von Monte-Carlo Simulationen (mit direkten Realisierungen)

import random
import math
import operator
import matplotlib
import matplotlib.pyplot as plt

##################################################################
#
#   Bandlücken und EnergieBreite der wichtigsten Halbleiter
#
#   Si    1.12    \sqrt(1.12)
#   Ge    0.66    \sqrt(0.66)
#   GaP   2.36    \sqrt(2.36)
#   GaAS  1.42    \sqrt(1.42)
#   InSb  0.18    \sqrt(0.18)
#   SiC   2.86    \sqrt(2.86)
#   GaN   3.39    \sqrt(3.39)
#   C     5.50    \sqrt(5.50)
#   SiO   8.00    \sqrt(8.00)
#
##################################################################

n_total = 1000000 # Variable für Anzahl der Monte-Carlo Iterationen

p0 = 4.5E3
norm = 1.0

Temperature = 300.0 # In Units of Kelvin 

DeltaEnergy = 1.12*1.60218E-19
WidthEnergy = math.sqrt(1.12*1.60218E-19)

VarDeltaEnergy = DeltaEnergy
StartDeltaEnergy = VarDeltaEnergy

ThermalEnergy = 1.38064852E-23*Temperature # In Units of Joule  
StartBandlueckenVerteilung = ThermalEnergy # Bei einem Wert von StartBandluecke = DeltaEnergy

BandlueckenVerteilungStatistics = []
factor = 1.0

for i in range(0, n_total):

    factor = random.gauss(1.0, math.sqrt(1.0))
    VarDeltaEnergy = math.fabs(factor)*DeltaEnergy
    BandlueckenVerteilung = (VarDeltaEnergy - DeltaEnergy)/WidthEnergy

    if (operator.gt(min((math.exp(-VarDeltaEnergy/ThermalEnergy)*math.exp(-BandlueckenVerteilung**2))/(math.exp(-StartDeltaEnergy/ThermalEnergy)*math.exp(-StartBandlueckenVerteilung**2)),1.00),random.uniform(0.00,1.00))):
                    
        BandlueckenVerteilungStatistics.append(p0*math.exp(-BandlueckenVerteilung**2)/math.sqrt(DeltaEnergy)*math.exp(-VarDeltaEnergy/ThermalEnergy))
        StartBandlueckenVerteilung = BandlueckenVerteilung
        StartDeltaEnergy = VarDeltaEnergy

plt.figure(1)
plt.hist(BandlueckenVerteilungStatistics, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 12)
plt.xlabel('$Elektronendichte~[1/cm^3]$', fontsize = 14)
plt.ylabel('$Wahrscheinlichkeit~p$', fontsize = 14)
plt.savefig('/Users/krealix/Desktop/IU_Internationale_Hochschule/DSGE0723/SourceCode/Figure2.png')                                                