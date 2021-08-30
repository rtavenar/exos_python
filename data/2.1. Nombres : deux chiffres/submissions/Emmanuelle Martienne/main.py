# Saisie d'un entier à deux chiffres (entre 10 et 99)
nb = int(input())
dizaine = nb // 10
unite = nb % 10
print("{0:d} {1:d}".format(dizaine,unite))
