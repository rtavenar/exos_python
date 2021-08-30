nb_lues = 0  # aucune valeur non nulle lue
somme = 0    # élement neutre de +
val = int(input())  # on lit la première valeur
while val != 0:
    nb_lues += 1  # elle est non nulle, on la compte
    somme += val  # et on l'ajoute à la somme
    val = int(input())  # et on lit la suivante
moyenne = somme / nb_lues
print(moyenne)


# cas du zéro en première place non traité !