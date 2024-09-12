#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention ssi la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ?")
chaine = False
while chaine == False:

 code_medals = input("Chaine représentant les médailles ?")
 for j in range(len(code_medals)) :

  if code_medals[j] == "G" or code_medals[j] == "S" or code_medals[j] == "B" :
    chaine = False
    print("Erreur dans l'entrée !")

  else :
   chaine = True


medaille_or = 0
medaille_argent = 0
medaille_bronze = 0 

for i in range(len(code_medals)):
 caractère = code_medals[i]


 if caractère == "G":
  medaille_or += 1

 if caractère == "S":
  medaille_argent += 1

 if caractère == "B":
  medaille_bronze += 1



 
    
print( str(medaille_or)+" Médailles d'or "+"\n"+ str(medaille_argent)+
     " Médaille d'argent "+"\n"+str(medaille_bronze)+
      " Médaille de bronze" )
