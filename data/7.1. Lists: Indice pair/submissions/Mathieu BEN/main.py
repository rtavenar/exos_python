# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)

a = [int(s) for s in input().split()]
  
print(" ".join([str(elem) for i,elem in enumerate(a) if i%2==0]))
  