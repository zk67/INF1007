# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Entrez la vitesse initiale: "))
angle = float(input("Entrez l'angle de lancement (en degrées): "))

distance = (pow(speed , 2) * math.sin(2* angle)) / 9.81

print("Distance parcourue: " + str(round(distance,2))+ "m")
