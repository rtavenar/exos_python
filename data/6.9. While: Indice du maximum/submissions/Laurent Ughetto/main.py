maxi = 0  # init avec une valeur < à la série
posmaxi = 0

val = int(input())  # on lit la première valeur
pos = 1  # ... qui est en position 1
while val != 0:
    if val > maxi:
        maxi = val  # elle est meilleur, on la conserve
        posmaxi = pos  # ainsi que sa position
    val = int(input())  # et on lit la suivante
    pos += 1  # ... qui est à  la position suivante
print(posmaxi)
