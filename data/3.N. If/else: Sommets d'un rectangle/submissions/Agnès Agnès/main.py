xa = int(input())
ya = int(input())

xb = int(input())
yb = int(input())

xc = int(input())
yc = int(input())

xd = -999
if xa == xb:
    xd = xc
if xa == xc:
    xd = xb
if xb == xc:
    xd = xa

yd = -999
if ya == yb:
    yd = yc
if ya == yc:
    yd = yb
if yb == yc:
    yd = ya

print(xd, yd)