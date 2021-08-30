# Read a string:
# s = input()
# Print a value:
# print(s)

d = {}
for i in range(int(input())):
  cand, nbvoix = input().split(" ")
  if cand not in d:
    d[cand] = 0
  d[cand] += int(nbvoix)
  
for cle, val in d.items():
  print(cle, val)
