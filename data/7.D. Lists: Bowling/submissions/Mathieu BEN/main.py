# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
N, K = tuple([int(s) for s in input().split()])
Q = ["I"]*N
#print(Q)
for i in range(K):
  start, stop = tuple([int(s) for s in input().split()])
  Q[start-1:stop] = ["."]*(stop-start+1)
  #print(Q)

print("".join(Q))
  