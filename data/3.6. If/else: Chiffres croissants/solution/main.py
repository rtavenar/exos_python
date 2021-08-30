x = int(input())
centaines = x // 100
dizaines = x // 10 % 10
unites = x % 10
if centaines < dizaines and dizaines < unites:
  print('OUI')
else:
  print('NON')