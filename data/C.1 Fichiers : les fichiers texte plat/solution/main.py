def compte_mots(nom_de_fichier):
  texte = open(nom_de_fichier, "r", encoding="utf-8").read()
  return len(texte.split())