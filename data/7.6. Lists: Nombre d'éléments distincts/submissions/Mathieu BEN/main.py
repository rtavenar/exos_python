# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]
nb = 1
before = a.pop(0)
for elem in a:
  if elem > before:
    nb+=1
  before = elem
print(nb)