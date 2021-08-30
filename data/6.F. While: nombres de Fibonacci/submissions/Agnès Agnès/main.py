n = int(input())
pred, cour = 1, 1
som = pred + cour
rang = 2
while rang < n:
    pred, cour = cour, som
    som = pred + cour
    rang += 1

print(cour)