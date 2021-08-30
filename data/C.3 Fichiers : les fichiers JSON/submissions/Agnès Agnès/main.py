import json

def compte_cles_prefixe(nom_du_fichier, prefixe):
  fp = open(nom_du_fichier, "r", encoding="utf-8")
  d=json.load(fp)
  cpt = 0
  for cle in d.keys():
    if cle.startswith(prefixe):
      cpt +=1
  return cpt