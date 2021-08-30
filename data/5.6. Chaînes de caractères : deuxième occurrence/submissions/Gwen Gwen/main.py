# Lire une chaîne de caractères :
s = input()
# Afficher une chaîne de caractères :
# print(s)
po = s.find("p")
nb = s.count("p")
if nb < 2 : print(nb-2)
else : print(s.find("p",po+1))
