# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)

a = [int(s) for s in input().split()]
nb = 0
for i in range(len(a)-1):
  for j in range(i+1, len(a)):
    if a[i] == a[j]:
      nb  +=1
      
print(nb)