# Read an integer:
# a = int(input())
# Print a value:
# print(a)

nbzero = 0
N = int(input())
for i in range(N):
  val = int(input())
  if val==0:
    nbzero+=1
print(nbzero)
