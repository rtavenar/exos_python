# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]

for i in range(1,len(a),2):
  a[i-1],a[i] = a[i],a[i-1]

for elem in a:
  print(elem, sep=" ")