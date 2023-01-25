from collections import Counter


def min_steps(s, t):
    return sum((Counter(s) - Counter(t)).values())


print(min_steps(s="bab", t="aba"))
