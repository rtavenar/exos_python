# Lire une chaîne de caractères :
s = input()
# Afficher une chaîne de caractères :
# print(s)
nb = s.count("f")
if nb == 0 : print(-1)
elif nb == 1 : print(s.index("f"))
else : print(s.index("f"),s.rfind("f"))
