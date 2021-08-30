ref_serie = 0  # valeur référence de la série
nb_serie = 0
maxi = 0
val = int(input())  # on lit la première valeur
while val != 0:
    if val == ref_serie:
        nb_serie += 1
    else:
        if nb_serie > maxi:
            maxi = nb_serie
        ref_serie = val
        nb_serie = 1
    val = int(input())  # et on lit la suivante
if nb_serie > maxi:
    maxi = nb_serie
print(maxi)
