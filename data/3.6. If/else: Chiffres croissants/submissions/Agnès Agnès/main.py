n = int(input())
c = n // 100   # extraction de la centaine
r = n % 100
d = r // 10    # extraction de la dizaine
u = r % 10     # extraction de l'unité
if c <= d and d <= u:
    print("OUI")
else:
    print("NON")