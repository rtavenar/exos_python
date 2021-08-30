aa = 2017
mm = int(input())
# nb de jours de chaque mois
l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if aa % 4 == 0:
    l[2] = 29
# l'indice d'un liste commence à 0
mm -= 1
print(l[mm])