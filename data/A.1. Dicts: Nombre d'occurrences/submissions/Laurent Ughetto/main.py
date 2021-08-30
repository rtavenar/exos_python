phrase = input()
l_mots = phrase.split()
d_occurences = {}
for mot in l_mots:
    if mot in d_occurences:
        d_occurences[mot] += 1
    else:
        d_occurences[mot] = 1
    print(d_occurences[mot] - 1)