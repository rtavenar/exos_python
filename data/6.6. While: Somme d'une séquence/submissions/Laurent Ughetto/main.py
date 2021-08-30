somme = 0  # élém neutre de la somme
val = int(input())  # on lit la première valeur
while val != 0:
    somme += val  # elle est non nulle, on l'ajoute à la somme
    val = int(input())  # et on lit la suivante
print(somme)
