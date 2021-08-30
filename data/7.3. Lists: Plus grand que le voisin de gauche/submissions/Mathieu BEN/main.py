# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]

before = a.pop(0)
for elem in a:
  if elem > before:
    print(elem, sep=' ')
  before = elem