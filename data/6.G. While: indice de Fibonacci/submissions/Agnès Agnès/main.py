n = int(input())  # supposé supérieur à 1

pred, cour = 1, 1
som = pred + cour
rang = 2
while som <= n:
    pred, cour = cour, som
    som = pred + cour
    rang += 1

if cour == n:
    print(rang)
else:
    print(-1)
