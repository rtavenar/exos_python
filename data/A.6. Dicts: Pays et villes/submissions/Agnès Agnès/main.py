d = {}
for p in range(int(input())):    # nb pays
    ligne = input().split(" ")   # pays vil1 vil2...
    d[ligne[0]] = ligne[1:]      # d[pays] = [vil1, vil2...]

for v in range(int(input())):    # nb villes
    ville = input()              # nom ville
    for p in d.keys():           # parcours par clé
        if ville in d[p]:
            print(p)
            break
