# Saisie du dictionnaire Français -> Latin
dfrlt = {}
for _ in range(int(input())):               # nb de lignes
    ligne = input().split(" - ")            # ligne francais - latin1, latin2, ...
    dfrlt[ligne[0]] = ligne[1].split(", ")  # d[francais] = [latin1, latin2...]
#print(dfrlt)

# Construction du dictionnaire Latin -> Français
dltfr = {}
for francais, lislatin in dfrlt.items():
    for latin in lislatin:
        if latin not in dltfr.keys():
            dltfr[latin] = []
        dltfr[latin].append(francais)
# print(dltfr)

# Affichage avec les tris alphabétiques
lg = len(dltfr.keys())
print(lg)
for motlat in sorted(list(dltfr.keys())):
    print(motlat, " - ", end='')
    nb = len(dltfr[motlat])
    i = 0
    for motfrn in sorted(dltfr[motlat]):
        print(motfrn, end="")
        i += 1
        if i < nb:
            print(", ", end="")
    print(' ')