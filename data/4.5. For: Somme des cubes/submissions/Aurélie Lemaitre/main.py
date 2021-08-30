# Read an integer:
# a = int(input())
# Print a value:
# print(a)

N = int(input())
somme=0
for i in range(1,N+1):
  somme+=i*i*i
print(somme)