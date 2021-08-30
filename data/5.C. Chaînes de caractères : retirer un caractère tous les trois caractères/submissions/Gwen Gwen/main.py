# Lire une chaîne de caractères :
s = input()
# Afficher une chaîne de caractères :
sres = "".join([s[i] for i in range(len(s)) if i%3 ])
print(sres)
