import csv

def nb_non_vides(nom_de_fichier):
  fp = open(nom_de_fichier, "r", encoding="utf-8")
  cpt = 0
  for ligne in csv.reader(fp, delimiter=";"):
    for cellule in ligne:
      if len(cellule) != 0:
        cpt +=1
  return cpt
