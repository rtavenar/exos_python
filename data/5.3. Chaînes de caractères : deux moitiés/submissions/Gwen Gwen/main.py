# Lire une chaîne de caractères :
s = input()
middle = len(s)//2+len(s)%2
deb = s[:middle]
fin = s[middle:]
# Afficher une chaîne de caractères :
print(fin+deb)
