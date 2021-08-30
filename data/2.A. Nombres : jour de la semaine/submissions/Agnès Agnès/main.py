k = int(input())   # num jour 1..365
n = k % 7 + 3      # le premier jour est un jeudi (4)
print(n % 7)