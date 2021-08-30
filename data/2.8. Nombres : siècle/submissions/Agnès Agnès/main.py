an = int(input())
siecle = an // 100
if an % 100 != 0:
    siecle += 1
print(siecle)