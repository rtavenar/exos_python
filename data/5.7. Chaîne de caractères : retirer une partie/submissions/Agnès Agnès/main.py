texte = input()
let = 'h'
deb = texte.find(let)
fin = texte.rfind(let)
print(texte[:deb] + texte[fin + 1 :])
