maxi = 0  # init avec une valeur < à la série
val = int(input())  # on lit la première valeur
while val != 0:
    if val > maxi:
        maxi = val  # elle est meilleur, on la conserve
    val = int(input())  # et on lit la suivante
print(maxi)
