debcol = int(input())
deblig = int(input())
fincol = int(input())
finlig = int(input())
if not(deblig == finlig and debcol == fincol) \
        and abs(finlig - deblig) == abs(fincol - debcol):
    print("oui")
else:
    print("non")