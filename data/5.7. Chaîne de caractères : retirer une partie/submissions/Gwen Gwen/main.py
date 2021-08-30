# Lire une chaîne de caractères :
s = input()
# Afficher une chaîne de caractères :
# print(s)
po = s.find("h")
do = s.rfind("h")
print(s[:po]+s[do+1:])
