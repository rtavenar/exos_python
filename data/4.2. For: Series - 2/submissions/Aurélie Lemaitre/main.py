# Read an integer:
a = int(input())
# Print a value:
# print(a)
b = int(input())
if(a<b):
  for i in range(a,b+1):
    print(i)
else:
  for i in range(a,b-1,-1):
    print(i)

