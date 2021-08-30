nb_val_pos = 0  # pas encore de valeur positive
val = int(input())  # on lit la première valeur
while val != 0:
    if val % 2 == 0:
        nb_val_pos += 1   # positive et paire : on la compte
    val = int(input())  # et on lit la suivante
print(nb_val_pos)
