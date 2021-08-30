# Read an integer:
# a = int(input())
# Print a value:
# print(a)

n = int(input())
sommefact=0
fact =1
for i in range(1,n+1):
  fact = fact*i
  sommefact +=fact
print(sommefact)