an = int(input())
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print("BISSEXTILE")
else:
    print("NORMALE")