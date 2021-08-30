def compte_mots(nom_de_fichier):
  fp = open(nom_de_fichier, "r", encoding="utf-8")
  cpt = 0
  lignes = fp.readlines()
  for ligne in lignes:
    lismots = ligne.split(" ")
    for mot in lismots:
      if len(mot) !=0:
        cpt +=1
  return cpt