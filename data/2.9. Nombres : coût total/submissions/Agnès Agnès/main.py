a = int(input())   # prix unitaire en euros
b = int(input())   # prix unitaire en centimes
n = int(input())   # nb de gâteaux
prixtot = (a + b / 100) * n
euro = int(prixtot)
cent = int(round(prixtot - euro, 2) * 100)
print(euro, cent)