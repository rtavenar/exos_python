# Read a string:
# s = input()
# Print a value:
# print(s)
d = {}
for i in range(int(input())):
  lig = input().split(" ")
  for mot in lig:
    if mot not in d:
      d[mot] = 0
    d[mot] += 1
    
motmax = " "
cptmax = 0
for mot, cpt in d.items():
  if (cpt > cptmax) or ((cpt == cptmax) and  (mot < motmax)):
    cptmax = cpt
    motmax = mot

print(motmax)    
    
  