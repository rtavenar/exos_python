texte = input()
carinit, carremp = 'h', 'H'
deb = texte.find(carinit) + 1
fin = texte.rfind(carinit)
gauche = texte[:deb]
centre = texte[deb:fin].replace(carinit, carremp)
droite = texte[fin:]
print(gauche + centre + droite)
