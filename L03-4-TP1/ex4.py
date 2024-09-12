import math
# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))

distance = 0
printDistance = True

if(battery_level == 0): 
    print("La batterie est vide")
    printDistance = False
while battery_level > 50:
    distance += 1
    battery_level -= .5
    #print(distance, battery_level)
while battery_level > 25:
    distance += 0.25
    battery_level -= 0.5
   # print(distance, battery_level)
while battery_level > 10:
    distance += .5
    battery_level -= .5
    #print(distance, battery_level)
while battery_level > 5:
    distance += 1.25
    battery_level -= 0.5
    #print(distance, battery_level)
while battery_level > 0:
    distance += 3
    battery_level -= 0.5
    #print(distance, battery_level)

# On affiche la distance seulement si la batterie est non vide
if(printDistance == True):print(f"{round(distance,1)} km")