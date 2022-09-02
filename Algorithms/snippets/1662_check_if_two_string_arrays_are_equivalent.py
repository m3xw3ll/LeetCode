def array_strings_are_equal(word1, word2):
    w1 = ''
    w2 = ''
    for i in word1:
        w1 += i
    for j in word2:
        w2 += j

    return w1 == w2

print(array_strings_are_equal(['ab', 'c'], ['a', 'bc']))