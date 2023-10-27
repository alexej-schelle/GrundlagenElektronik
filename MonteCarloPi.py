###############################################################################################################################################
#                                                                                                                                             #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                             #
###############################################################################################################################################

# Grundlegendes Anwendungsbeispiel für die Modellierung mithilfe von Monte-Carlo Simulationen (mit direkten Realisierungen)

import random
import math

n_total = 0 # Variable für Anzahl der Ereignisse innerhalb eines Einheits-Rechtecks 
n_hits = 0 # Variable für Anzahl der Ereignisse innerhalb eines Einheits-Kreises

a = 1.0

while (1 < 2):

    m = random.uniform(-a,a) # Generiere Zufallszahl m mit Gleichverteilung
    n = random.uniform(-a,a) # Generiere Zufallszahl n mit Gleichverteilung

    n_total = n_total + 1 # Zähler für die Anzahl der Ereignisse innerhalb eines Einheits-Rechtecks 
    
    if (m**2 + n**2 < a**2) : n_hits = n_hits + 1 # Zähler für die Anzahl der Ereignisse innerhalb eines Einheits-Kreises

    if (math.fabs(4.0*float(n_hits)/float(n_total) - math.pi) < 1.0E-7): # Abweichung der berechneten Kreiszahl zur bereits bekannten Kreiszahl

        print(int(n_total)) # Anzahl der benötigten Rechenschritte
        print(round(4.0*float(n_hits)/float(n_total),7)) # Berechnete Kreiszahl pi

        break

print(math.pi) # Rückgabewert der berechneten Kreiszahl pi


