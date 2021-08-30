a = [int(s) for s in input().split()]
found = False
for i in range(1, len(a)):
  if a[i - 1] * a[i] > 0:
    print(a[i - 1], a[i])
    found = True
    break
if not found :
  print(0)