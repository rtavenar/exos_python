# Saisie d'un entier à deux chiffres (entre 10 et 99)
nb = int(input())
dizaine = nb // 10
unite = nb % 10
nbinv = (unite*10)+dizaine
print("{0:d}".format(nbinv))