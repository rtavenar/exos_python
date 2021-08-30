# Lire une chaîne de caractères au clavier :
# s = input()
# Afficher la valeur de s :
# print(s)
listeEntiers = [int(entier) for entier in input().split()]
print(len(set(listeEntiers)))