texte = input()
let = 'h'
deb = texte.find(let)
fin = texte.rfind(let)
centre = texte[deb:fin+1]
print(texte[:deb] + centre[::-1] + texte[fin + 1 :])