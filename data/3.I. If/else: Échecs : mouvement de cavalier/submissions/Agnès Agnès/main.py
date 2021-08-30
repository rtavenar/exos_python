def depl_en_L(fin1, deb1, fin2, deb2):
    return abs(fin1 - deb1) == 2 and abs(fin2 - deb2) == 1


debcol = int(input())
deblig = int(input())
fincol = int(input())
finlig = int(input())

if depl_en_L(finlig, deblig, fincol, debcol) \
        or depl_en_L(fincol, debcol, finlig, deblig):
    print("OUI")
else:
    print("NON")
    
