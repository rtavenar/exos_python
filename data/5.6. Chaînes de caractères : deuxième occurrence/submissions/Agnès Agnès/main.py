mot = input()
let = 'p'
if let in mot:
    pos1 = mot.find(let)
    mot2 = mot[pos1+1:]
    if let in mot2:
        print(mot2.find(let) + pos1 + 1)
    else:
        print(-1)
else:
    print(-2)
