from collections import defaultdict


def num_equiv_domino_pairs(dominoes):
    dict = defaultdict(int)
    out = 0
    for d1, d2 in dominoes:
        k = min(d1, d2), max(d1, d2)
        out += dict[k]
        dict[k] += 1
    return out


print(num_equiv_domino_pairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
