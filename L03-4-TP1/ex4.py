import math
# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Quel est le pourcentage de la batterie ? "))

distance = 0
if(battery_level == 0): print("La batterie est vide\n")
while battery_level > 50:
    distance += 2
    battery_level -= 1
while battery_level > 25:
    distance += 0.5
    battery_level -= 1
while battery_level > 10:
    distance += 1
    battery_level -= 1
while battery_level > 5:
    distance += 2.5
    battery_level -= 1
while battery_level > 0:
    distance += 6
    battery_level -= 1


print(f"Distance pouvant être parcourue: {math.trunc(distance)} km")