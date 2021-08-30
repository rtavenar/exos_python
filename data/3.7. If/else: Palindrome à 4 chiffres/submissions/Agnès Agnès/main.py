nb = int(input())
q = nb
chiffres = []  # chaque chiffre du nombre sera mis dans cette liste

# division des quotients successifs- arrêt quand q == 0
while q != 0:
    chiffres.append(q % 10)
    q = q // 10

# nombre de tours de boucle : la moitié du nombre de chiffres
n = len(chiffres) // 2
lg = len(chiffres)
palindrome = "OUI"
for i in range(n):
    if chiffres[i] != chiffres[lg - i - 1]:
        palindrome = "NON"
        break
print(palindrome)