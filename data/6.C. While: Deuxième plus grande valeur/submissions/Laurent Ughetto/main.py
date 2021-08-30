max1 = 0  # init avec une valeur < à la série
max2 = 0
val = int(input())  # on lit la première valeur
while val != 0:
    if val > max1:
        max2 = max1
        max1 = val
    elif val > max2:
        max2 = val
    val = int(input())  # et on lit la suivante
print(max2)
