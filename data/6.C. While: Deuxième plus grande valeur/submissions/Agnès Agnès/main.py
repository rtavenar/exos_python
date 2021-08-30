# hypothèse : les deux premières valeurs ne sont pas à 0
maxpred = int(input())
maxsuiv = int(input())
if maxpred > maxsuiv:
    maxpred, maxsuiv = maxsuiv, maxpred

n = int(input())
while n != 0:
    if n > maxsuiv:
        maxpred, maxsuiv = maxsuiv, n
    elif n > maxpred:
        maxpred = n
    
    n = int(input())
print(maxpred)
