def merge_alternately(word1, word2):
    l = max(len(word1), len(word2))
    out = ''
    word1 = word1.ljust(l, ' ')
    word2 = word2.ljust(l, ' ')
    for i in range(0, l):
        out += word1[i] + word2[i]
    return out.replace(' ', '')


print(merge_alternately('abc', 'pqr'))