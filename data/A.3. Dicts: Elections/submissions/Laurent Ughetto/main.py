d_voix = {}

nb_enreg = int(input())

for enreg in range(nb_enreg):
    candidat, voix = input().split()
    if candidat in d_voix.keys():
        d_voix[candidat] += int(voix)
    else:
        d_voix[candidat] = int(voix)

for candidat, voix in sorted(d_voix.items()):
    print(candidat, voix)
    