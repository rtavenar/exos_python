# Saisie d'un millésime
annee = int(input())
siecle = annee // 100
if (annee % 100 != 0):
  siecle +=1
print("{0:d}".format(siecle))
