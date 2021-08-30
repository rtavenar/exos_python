n = int(input())
som = 0
fact = 1
for i in range(1, n+1):
    fact *= i
    som += fact
print(som)