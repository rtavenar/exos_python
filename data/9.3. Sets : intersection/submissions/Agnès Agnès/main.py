def creerSetEntiers():
    l = input().split()  # liste de nb sous forme de chaine de car
    return set(int(e) for e in l) # creation d'un set de nb convertis de ch à entier


s1 = creerSetEntiers()
s2 = creerSetEntiers()
for elt in sorted(s1 & s2):
    print(elt, end =' ')
