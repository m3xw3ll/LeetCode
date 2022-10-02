from collections import Counter


def equal_frequency(word):
    c = Counter(word)
    for i in word:
        c[i] -= 1

        if c[i] == 0:
            c.pop(i)

        if len(set(c.values())) == 1:
            return True
        c[i] += 1
    return False


print(equal_frequency('abcc'))
