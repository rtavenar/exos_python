maxi = int(input())
nb = 1
sq = 1
ch = ''
while sq <= maxi:
   ch += str(sq) + ' '
   nb += 1
   sq = nb * nb
print(ch)
