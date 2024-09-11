# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")

athlete = input("Quel est le nom de l'athlète ? ")

date = input("Quelle est la date du record ? ")

dicipline = input("Quelle est la dicipline de l'athlète ? ")

catégorie = input("Quelle est la catégorie de l'athlète ? ")

record = input("Quel est le record ? ")

print("\n"+"Nouveau Record:"+"\n"
       +"------------------"+ "\n" 
       +date + " - " + dicipline + " - " + catégorie + ":" + "\n"
       +athlete+" ("+country+") - " + record) 

#IT IS WORKING!!!!