# Saisie de données
prixeuros = int(input())
prixcent = int(input())
nbgateaux = int(input())
centimes = ((prixeuros*100) + prixcent) * nbgateaux
totaleuros = centimes // 100
totalcent = centimes % 100
print("{0:d} {1:d}".format(totaleuros,totalcent))
