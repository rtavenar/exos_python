# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]
emax = a[0]
imax = 0
for i in range(1,len(a)):
  if a[i] > emax:
    emax = a[i]
    imax = i
    
print(emax, imax)
  