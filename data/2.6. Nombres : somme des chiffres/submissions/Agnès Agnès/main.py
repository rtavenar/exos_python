n = int(input())
centaine = n // 100
n = n % 100
dizaine = n // 10
unite = n % 10
print(centaine + dizaine + unite)