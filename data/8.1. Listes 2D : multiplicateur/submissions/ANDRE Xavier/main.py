# Lire une liste 2D d'entiers :
# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
# Afficher la valeur de a :
# print(a)
m, n = input().split()
m, n = int(m), int(n)

a = [[int(j) for j in input().split()] for i in range(m)]

c =  int(input())

for ligne in a :
  ligneFois2=[]
  for elem in ligne :
    ligneFois2.append(str(c*elem))
  print(' '.join(ligneFois2))
