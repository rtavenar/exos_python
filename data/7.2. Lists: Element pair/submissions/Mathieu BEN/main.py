# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]

for elem in a:
  if elem%2==0 :
    print(elem, sep=' ')
