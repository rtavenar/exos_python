# Lire une chaîne de caractères :
s = input()
# Afficher une chaîne de caractères :
# print(s)
po = s.find("h")
do = s.rfind("h")
mi = s[po:do+1]
print(s[:po]+mi[::-1]+s[do+1:])