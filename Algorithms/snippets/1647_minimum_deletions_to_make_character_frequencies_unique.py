from collections import Counter


def min_deletions(s):
    c = Counter(s)
    seen = set()
    cnt = 0
    for value, freq in c.items():
        while freq > 0 and freq in seen:
            freq -= 1
            cnt += 1
        seen.add(freq)
    return cnt


print(min_deletions('aaabbbcc'))