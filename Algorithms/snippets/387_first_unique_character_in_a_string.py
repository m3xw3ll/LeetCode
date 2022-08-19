from collections import Counter


def first_unique_char(s):
    c = Counter(s)
    for i, char in enumerate(s):
        if c[char] == 1:
            return i
    return -1


print(first_unique_char('leetcode'))