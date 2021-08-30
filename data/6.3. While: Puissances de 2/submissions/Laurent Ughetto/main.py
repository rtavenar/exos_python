X = int(input())
n = 0
puiss2 = 1
while puiss2 <= X:
  n += 1
  puiss2 *= 2
n -= 1
puiss2 //= 2
print(n, puiss2)
