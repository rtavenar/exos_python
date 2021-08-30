l = input().split()
s = set()
for e in l:
    if e in s:
        print("YES")
    else:
        print("NO")
    s.add(e)
