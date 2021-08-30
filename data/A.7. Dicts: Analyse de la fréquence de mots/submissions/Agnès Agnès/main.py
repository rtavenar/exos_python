d = {}
for _ in range(int(input())):     # nb de lignes
    ligne = input().split(" ")    # ligne est une liste de mots
    for mot in ligne:
        if mot not in d:
            d[mot] = 0
        d[mot] += 1                 # comptage de chaque mot


l = []
for cle, val in d.items():
    l.append([val, cle])


# tri sur deux critères la valeur inversée puis la clé
ltri =sorted(l, key=lambda x: (-x[0], x[1]))

# affichage
for lig in ltri:
   print(lig[1], lig[0])
  