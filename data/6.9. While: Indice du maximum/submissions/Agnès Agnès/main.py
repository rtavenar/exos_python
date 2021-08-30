maxval, maxind, nb = -1, -1, 0
n = int(input())

while n != 0:
    nb += 1
    if maxval < n:
        maxval = n
        maxind = nb
    n = int(input())

print(maxind)
