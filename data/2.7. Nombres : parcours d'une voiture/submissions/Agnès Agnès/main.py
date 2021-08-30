n = int(input())
m = int(input())
nbjours = m // n
if m % n != 0:
    nbjours += 1
print(nbjours)