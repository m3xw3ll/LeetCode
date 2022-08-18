from collections import Counter


def unique_occurrences(arr):
    c = Counter(arr)
    occ = list()
    for i, j in c.items():
        occ.append(j)
    return True if (len(set(occ))) == len(occ) else False


print(unique_occurrences([1, 2, 2, 1, 1, 3]))
