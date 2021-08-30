n = -1
som, nb = 0, 0
while n != 0:
    n = int(input())
    som += n
    nb += 1
print(som / (nb - 1))