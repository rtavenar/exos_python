motinit = input()
motreduit = ''
for i in range(len(motinit)):
    if i % 3 != 0:
        motreduit += motinit[i]
print(motreduit)
