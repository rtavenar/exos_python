def surplace():
    return (finlig == deblig) and (fincol == debcol)


def dep_droit():
    return (debcol == fincol) or (deblig == finlig)


def dep_diag():
    return abs(finlig - deblig) == abs(fincol - debcol)


debcol = int(input())
deblig = int(input())
fincol = int(input())
finlig = int(input())
if (not surplace()) and (dep_droit() or dep_diag()):
    print("OUI")
else:
    print("NON")