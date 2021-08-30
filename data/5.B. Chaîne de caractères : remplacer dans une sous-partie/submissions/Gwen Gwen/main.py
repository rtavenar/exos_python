# Read a string:
s = input()
# Print a string:
# print(s)
po = s.find("h")
do = s.rfind("h")
mi = s[po+1:do]
print(s[:po+1]+mi.replace("h","H")+s[do:])
