a = int(input())
b = int(input())
if a < b:
    pas = 1
    fin = b + 1
else:
    pas = -1
    fin = b - 1
for i in range(a, fin, pas):
    print(i, end=" ")
