# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
a = [int(s) for s in input().split()]
imin = a.index(min(a))
imax = a.index(max(a))
a[imin], a[imax] = a[imax], a[imin]
print(*a)