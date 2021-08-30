import json

def compte_cles_prefixe(nom_du_fichier, prefixe):
  d = json.load(open(nom_du_fichier, "r", encoding="utf-8"))
  n = 0
  for k in d.keys():
    if k.startswith(prefixe):
      n += 1
  return n
