###############################################################################################################################################
#                                                                                                                                             #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                             #
###############################################################################################################################################

# Berechnung der Energieniveaus im Wasserstoffatom

import random
import math

N = 100

Energy = [0.0]*N
EnergyLevels = [0.0]*N
EnergyGap = [0.0]*N

Energy[0] = -13.6 # In units of ElektronenVolt

for l in range(1,N):

    Energy[l] = -13.6 / l**2
    EnergyLevels[l] = Energy[l] - Energy[l-1]
    EnergyGap[l] = Energy[l] - Energy[0]

print(Energy)
print(EnergyLevels)
print(EnergyGap)