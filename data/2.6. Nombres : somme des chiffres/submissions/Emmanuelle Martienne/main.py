# Saisie d'un nombre entier
nb = int(input())
somme = (nb % 10) + ((nb // 10) % 10) + (((nb // 10) // 10) % 10)
print("{0:d}".format(somme))
