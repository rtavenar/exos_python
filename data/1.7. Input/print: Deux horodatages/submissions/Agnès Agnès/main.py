
hdeb = int(input())
mdeb = int(input())
sdeb = int(input())
hfin = int(input())
mfin = int(input())
sfin = int(input())
tdeb = ((hdeb * 60 + mdeb) * 60) + sdeb
tfin = ((hfin * 60
+ mfin) * 60) + sfin
print(tfin - tdeb)