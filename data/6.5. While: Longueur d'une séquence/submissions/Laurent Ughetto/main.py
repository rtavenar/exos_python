nb_lues = 0  # aucune valeur non nulle lue
val = int(input())  # on lit la première valeur
while val != 0:
    nb_lues += 1  # elle est non nulle, on la compte
    val = int(input())  # et on lit la suivante
print(nb_lues)
