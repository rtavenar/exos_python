s = input()

# Sur la première ligne, afficher le troisième caractère de cette chaîne
print(s[2])
# Sur la seconde ligne, afficher du deuxième jusqu'au dernier
# caractère de cette chaîne.
print(s[1:])
# Sur la troisième ligne, afficher les cinq premiers caractères de la chaîne.
print(s[0:5])
# Sur la quatrième, afficher tous les caractères sauf les deux derniers de la chaîne.
print(s[:-2])
# Sur la cinquième ligne, afficher tous les caractères d'indices pairs
# (attention, se rappeler que les indices commencent à 0,
# donc les caractères sont affichés en commençant par le premier).
print(s[::2])
# Sur la sixième ligne, afficher les caractères de la chaîne,
# tous les deux caractères et en commençant par le second caractère de la chaîne.
print(s[1::2])
# Sur la septième ligne afficher tous les caractères de la chaîne en sens inverse.
print(s[::-1])
# Sur la huitième ligne, afficher la chaîne à l'envers,
# tous les deux caractères, en commençant par le dernier.
print(s[::-2])
# Sur la neuvième ligne, afficher la longueur de la chaîne saisie.
print(len(s))