debcol = int(input())
deblig = int(input())
fincol = int(input())
finlig = int(input())
if not(deblig == finlig and debcol == fincol)\
   and (finlig in range(deblig - 1, deblig +2))\
   and (fincol in range(debcol - 1, debcol +2)):
    print("oui")
else:
    print("non")