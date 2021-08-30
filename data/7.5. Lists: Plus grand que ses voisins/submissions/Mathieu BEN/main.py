# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)

a = [int(s) for s in input().split()]
nb = 0
for i in range(len(a)):
  if i>0 and i<len(a)-1 and a[i-1]<a[i] and a[i+1]<a[i]:
    nb +=1
print(nb)    
