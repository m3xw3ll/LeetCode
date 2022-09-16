def uncommon_from_sentences(s1, s2):
    ss = s1.split() + s2.split()
    d = {}
    for w in ss:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1

    return [w for w in d if d[w] == 1]


print(uncommon_from_sentences('this apple is sweet', 'this apple is sour'))