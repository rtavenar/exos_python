nb_paires = int(input())
dico = {}
for i in range(nb_paires):
    paire = input().split()
    dico[paire[0]] = paire[1]
mot = input()
if mot in dico.values():
    print(list(dico.keys())[list(dico.values()).index(mot)])
elif mot in dico.keys():
    print(dico[mot])