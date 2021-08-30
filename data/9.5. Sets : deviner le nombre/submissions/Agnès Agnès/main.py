n = int(input())         # valeur max du nombre secret
aide = False
trouve = False
srefus = set()                # ens destiné à contenir tous les éléments rejetés
saccep = set(range(1, n+1))   # ens destiné aux éléments candidats, init à tous les éléments de 1 à n

while (not(aide) and not(trouve)):
    rep_bea = input()
    if rep_bea.upper() == "HELP":
        aide = True
    else:
        s = set(int(e) for e in rep_bea.split())
        rep_aug = input()
        if rep_aug.upper() == "YES":
            saccep = saccep & s   # intersection de deux sets
            if len(saccep) == 1:
                trouve = True
                # print("Bravo trouve")
        else:
            srefus = srefus | s    # union de deux sets
#    print("R", *sorted(srefus))
#    print("A", *sorted(saccep))

# if trouve:
#     print("Bravo, c'est bien : ", *saccep)
# else:
#     print(*sorted(saccep - srefus))
print(*sorted(saccep - srefus))