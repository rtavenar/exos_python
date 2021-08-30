# Définition des droits d'accès
dicodef = {}
for i in range(int(input())):
  lis = input().split(" ")
  cle = lis[0]
  val = lis[1:]
  dicodef[cle] = val
# Les demandes d'accès  
dicodroit = { 
  "read"    : "R",
  "write"   : "W",
  "execute" : "X"
  }

for j in range(int(input())):
  droitlu, nomfic = input().split(" ")
  droit = dicodroit[droitlu]
  if nomfic not in dicodef:
    print("Access denied")
  else:
    if droit in dicodef[nomfic]:
      print(" OK")
    else:  
      print("Access denied")