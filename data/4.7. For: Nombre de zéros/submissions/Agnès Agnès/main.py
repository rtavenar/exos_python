n = int(input())
nbzeros = 0
for _ in range(n):
    if  int(input()) == 0:
        nbzeros += 1
print(nbzeros)
