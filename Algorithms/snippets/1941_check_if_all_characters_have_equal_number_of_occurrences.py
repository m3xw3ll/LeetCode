from collections import Counter

def are_occurrendes_equal(s):
    c = Counter(s)
    return True if len(set(c.values())) == 1 else False


print(are_occurrendes_equal('aaabb'))
