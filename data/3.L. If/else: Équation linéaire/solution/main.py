a = int(input())
b = int(input())

if a == 0:
  if b == 0:
    print('multiples solutions')
  else:
    print('pas de solution')
elif b % a == 0:
  print(b // a)
else:
  print('pas de solution')
