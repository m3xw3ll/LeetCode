def sort_sentence(s):
    words = s.split(' ')
    d = {}
    out = []
    for word in words:
        d[int(word[-1])] = word[:-1]
    for i in range(1, len(words) + 1):
        out.append(d[i])
    return ' '.join(out)


print(sort_sentence('is2 sentence4 This1 a3'))
