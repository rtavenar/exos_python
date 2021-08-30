nbplusgrands = 0
courant = int(input())
suivant = int(input())
while suivant != 0:
    if courant < suivant:
        nbplusgrands += 1
    courant = suivant
    suivant = int(input())
print(nbplusgrands)