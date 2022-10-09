import string
from collections import Counter

def check_almost_equivalent(word1, word2):
    w1 = Counter(word1)
    w2 = Counter(word2)

    for char in string.ascii_lowercase:
        if abs(w1[char] - w2[char]) > 3:
            return False
    return True


print(check_almost_equivalent('aaaa', 'bccb'))