def odd_string(words):
    out = list()
    for word in words:
        d = list()
        for i in range(len(word) - 1):
            d.append(ord(word[i+1]) - ord(word[i]))
        out.append(tuple(d))

    for t in list(set(out)):
        if out.count(t) == 1:
            return words[out.index(t)]


print(odd_string(["adc", "wzy", "abc"]))
