maxval = -1
n = int(input())
while n != 0:
    if n > maxval:
        maxval = n
        maxcpt = 1
    elif n == maxval:
        maxcpt += 1

    n = int(input())
print(maxcpt)
