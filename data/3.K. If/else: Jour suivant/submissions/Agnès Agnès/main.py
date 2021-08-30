lnbjour=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

jour = int(input())
mois = int(input())

joursuiv = jour + 1
if joursuiv > lnbjour[mois]:
    joursuiv = 1
    mois = mois + 1
    if mois > 12:
        mois = 1
print(joursuiv, mois)