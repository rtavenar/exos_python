maxi = 0  # init avec une valeur < à la série
nb_maxi = 0

val = int(input())  # on lit la première valeur
while val != 0:
    if val > maxi:
        maxi = val  # elle est meilleur, on la conserve
        nb_maxi = 1
    elif val == maxi:
        nb_maxi += 1
    val = int(input())  # et on lit la suivante
print(nb_maxi)
