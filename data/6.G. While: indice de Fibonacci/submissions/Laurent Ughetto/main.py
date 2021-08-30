nb_a_trouver = int(input())
rang = -1

prec_2 = prec_1 = 1
nb = 2
while rang == -1 and nb_a_trouver >= prec_1:
    if nb_a_trouver == prec_1:
        rang = nb
    nb += 1
    prec_2, prec_1 = prec_1, prec_1 + prec_2
#print(rang)

# à la place de l'affichage standard :
if nb_a_trouver == 1:
    print('coucou') # ce cas n'est pas testé !!!
else:
    print(rang)