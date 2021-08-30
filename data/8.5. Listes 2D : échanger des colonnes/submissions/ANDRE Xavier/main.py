# Lire une liste 2D d'entiers :
# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
# Afficher la valeur de a :
# print(a)
m, n = input().split()
m, n = int(m), int(n)
#m, n = 3, 4

a = [[int(j) for j in input().split()] for i in range(m)]
#a = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

i, j = input().split()
i, j = int(i), int(j)
#i, j = 0, 1

for ligne in range(m) :
  for colonne in range(n) :
    if colonne == i :
      a[ligne][i], a[ligne][j] = a[ligne][j], a[ligne][i]

for ligne in a :
  print(' '.join([str(elem) for elem in ligne]))
