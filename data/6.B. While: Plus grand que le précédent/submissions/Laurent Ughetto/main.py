val_prec = int(input())
val = int(input())
nb = 0
while val != 0:
    if val > val_prec:
        nb += 1
    val_prec = val
    val = int(input())
print(nb)
