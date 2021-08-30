n = int(input())
if n == 1 or n== 2:
    print(1)
else:
    prec_2 = 1
    prec_1 = 1
    nb = 2
    while nb < n:
        nb += 1
        prec_2, prec_1 = prec_1, prec_1 + prec_2
    print(prec_1)