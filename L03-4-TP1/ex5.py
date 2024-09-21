#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention ssi la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")



code_medals = input("Chaine représentant les médailles ? ")


chaine = True

for j in range(len(code_medals)) :

  if code_medals[j] not in {"G", "S", "B"}:
    print("Ceci est une chaine invalide.")
    chaine = False

    



medaille_or = 0
medaille_argent = 0
medaille_bronze = 0 


if chaine == True :

   for i in range(len(code_medals)):
    caractère = code_medals[i]


    if caractère == "G":
     medaille_or += 1

    if caractère == "S":
     medaille_argent += 1

    if caractère == "B":
     medaille_bronze += 1



 
    
   print( country+":"
     "\n- "+str(medaille_or)+" Or\n- "+str(medaille_argent)+" Argent\n- "+str(medaille_bronze) +" Bronze"  )
