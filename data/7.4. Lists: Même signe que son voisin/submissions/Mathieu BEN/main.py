# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]
before = a.pop(0)
paire = "0"
for elem in a:
  if before*elem>0:
    paire = str(before)+" "+str(elem)
    break
  before = elem
print(paire)