# Read an integer:
# a = int(input())
# Print a value:
# print(a)

N = int(input())
l = [int(input())for i in range(N-1)]

for i in range(1,N+1):
  if i not in l :
    print( i)
    break