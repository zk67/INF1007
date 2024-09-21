# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")

athlete = input("Quel est son nom ? ")

date = input("Date du record ? ")

dicipline = input("Dans quelle discipline ? ")

catégorie = input("Dans une catégorie spécifique ? ")

record = input("Quel est le record ? ")

print(f"\nNouveau Record:\n--------------------\n{date} - {dicipline} - {catégorie}:\n\t{athlete} ({country}) - {record}") 
