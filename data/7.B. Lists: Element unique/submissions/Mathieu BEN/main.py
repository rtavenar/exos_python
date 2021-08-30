# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)

a = [int(s) for s in input().split()]

for e in a:
  if a.count(e) == 1:
    print(e, sep=' ')