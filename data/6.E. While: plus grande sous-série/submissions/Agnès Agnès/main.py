pred = int(input())
cour = int(input())
maxi, lg = 1, 1

while cour != 0:

    if pred != cour:
        if lg > maxi:
            maxi = lg
        lg = 1
    else:
        lg += 1
    pred = cour
    cour = int(input())

if lg > maxi:
    maxi = lg
print(maxi)