# Saisie des données
nba = int(input())
nbb = int(input())
nbc = int(input())
bura = (nba // 2) + (nba % 2)
burb = (nbb // 2) + (nbb % 2)
burc = (nbc // 2) + (nbc % 2)
totalbur = bura+burb+burc
print("{0:d}".format(totalbur))
