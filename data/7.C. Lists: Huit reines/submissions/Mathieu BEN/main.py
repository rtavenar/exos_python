# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
coord = []
res = "NO"
for i in range(8):
  coord.append([int(s) for s in input().split()])

for i in range(8):
  for j in range(i+1,8):
    if coord[i][0] == coord[j][0] or coord[i][1] == coord[j][1] or coord[i][0]-coord[i][1] == coord[j][0]-coord[j][1] or coord[i][0]+coord[i][1] == coord[j][0]+coord[j][1]:
      res = "YES"
      break
print(res)
