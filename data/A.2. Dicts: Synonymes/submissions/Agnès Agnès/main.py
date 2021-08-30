# Read a string:
# s = input()
# Print a value:
# print(s)

n = int(input())
d = {}
dinv = {}
for i in range(n):
  tex = input()
  cle, val = tex.split(" ")
  d[cle] = val
  dinv[val] = cle

mot = input() 
if mot in d:
  print(d[mot])
if mot in dinv:
  print(dinv[mot])

  