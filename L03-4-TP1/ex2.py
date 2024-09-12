import math

# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = input("Quelle quantité d'eau faut-il assainir ? ")
ratio = float(water_quantity)/5
nbfiltres = ratio
nblampes = 3*ratio
if nbfiltres-int(nbfiltres) > 0:nbfiltres +=1
if nblampes-int(nblampes) > 0:nblampes += 1

print(f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:\n
        \t- Filtre(s) : {int(nbfiltres)}\n
        \t- Lampe(s) UV : {int(nblampes)}\n
        \t- Chlore : {ratio * 0.5}kg""")


    