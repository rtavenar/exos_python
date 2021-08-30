# Saisie des données
nbtotalmin = int(input())
nbheures = nbtotalmin // 60
nbmin = nbtotalmin % 60
print("{0:d} {1:d}".format(nbheures,nbmin))