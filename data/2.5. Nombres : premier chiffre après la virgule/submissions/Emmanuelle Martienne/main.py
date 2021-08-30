# import de la fonction floor() du module math qui retourne la partie entière d'un nombre décimal
from math import floor
# Saisie d'un réel
nb = float(input())
chiffre = floor(nb*10) % 10
print("{0:d}".format(chiffre))
