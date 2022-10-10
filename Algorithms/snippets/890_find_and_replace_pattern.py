from collections import defaultdict

def make_pattern(word):
    dic = {}
    p = list()
    cnt = 0

    for char in word:
        if char not in dic:
            dic[char] = cnt
            cnt += 1
        p.append(dic[char])
    return p


def find_and_replace_pattern(words, pattern):
    pat = make_pattern(pattern)
    return [word for word in words if make_pattern(word) == pat]


print(find_and_replace_pattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], 'abb'))
