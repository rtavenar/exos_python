n = int(input())
s = set(range(n + 1)) - {0}

for _ in range(1, n):
    e = int(input())
    s -= {e}

for val in s:
    print(val)