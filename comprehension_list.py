# On créé une liste de 0 à 99 éléments avec range
liste_1 = range(99)

# On récupère uniquement les nombres pairs
comp_list = [i for i in liste_1 if i%2 == 0]

# on check le résultat
print(comp_list)