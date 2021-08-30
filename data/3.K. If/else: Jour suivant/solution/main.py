jour = int(input())
mois = int(input())

if ((jour == 30) and (mois == 4 or mois == 6 or mois == 9 or mois == 11)
    or (jour == 28) and (mois == 2)
    or (jour == 31)):
  mois += 1
  jour = 1
else:
  jour += 1
if mois == 13:
  mois = 1

print(jour)
print(mois)