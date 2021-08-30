a = int(input())
b = int(input())

if a == 0:
    if b == 0:
        print("multiples solutions")
    else:
        print("pas de solution")
else:
    x = b // a
    if a * x == b:
        print(x)
    else:
        print("pas de solution")