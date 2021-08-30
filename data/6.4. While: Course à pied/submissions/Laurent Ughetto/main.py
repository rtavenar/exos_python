x = int(input())
y = int(input())

nbjours = 1  # on cours x le 1er jour !
while x < y:
  x *= 1.1
  nbjours += 1
print(nbjours)
