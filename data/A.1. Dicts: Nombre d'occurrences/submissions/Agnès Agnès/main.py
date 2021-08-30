# Read a string:
s = input()
espace = " " 
lismots = s.split(espace)
d = {}
for mot in lismots:
  if mot in d:
    d[mot] +=1
  else:
    d[mot] = 0
  print(d[mot])
