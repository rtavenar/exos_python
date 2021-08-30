x = int(input())
milliers = x // 1000
centaines = x // 100 % 10
dizaines = x // 10 % 10
unites = x % 10
if milliers == unites and centaines == dizaines:
  print('OUI')
else:
  print('NON')