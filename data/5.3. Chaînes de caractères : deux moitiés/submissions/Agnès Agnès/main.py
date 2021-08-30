from math import ceil

s = input()
moitie = ceil(len(s) / 2)    # ceil arrondi à l'entier supérieur
print(s[moitie:] + s[:moitie])
