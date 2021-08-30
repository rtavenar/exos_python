mot = input()
let = 'f'
indmin, indmax = -1, -1
dern = len(mot) - 1
moitie = len(mot) + 1 // 2
for i in range(moitie):
    if mot[i] == let and indmin == -1:
        indmin = i
    if  mot[dern - i] == let and indmax == -1:
        indmax = dern - i
    if indmin != -1 and indmax != -1:
        break
if indmin == indmax:
    print(indmin)
else:
    print(indmin, indmax)