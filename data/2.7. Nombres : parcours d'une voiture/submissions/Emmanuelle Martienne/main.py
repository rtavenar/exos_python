# Saisie des données
nbKjour = int(input())
distance = int(input())
nbjours = distance // nbKjour
if (distance % nbKjour != 0):
  nbjours += 1
print("{0:d}".format(nbjours))