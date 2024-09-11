# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = input("Quelle quantité d'eau faut-il assainir? ")
ratio = int(water_quantity)/5
print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:")
print(f"\t- Filtres: {ratio}")
print(f"\t- Lampes UV: {ratio *3}")
print(f"\t- Chlore: {ratio * 0.5}kg")

