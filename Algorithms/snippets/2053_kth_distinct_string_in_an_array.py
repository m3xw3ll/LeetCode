from collections import Counter


def kth_distinct(arr, k):
    c = dict(Counter(arr))
    out = []
    print(c)
    for i in c:
        if (c[i]) == 1:
            out.append(i)
    print(out)
    if len(out) < k:
        return ""
    return out[k - 1]


print(kth_distinct(["d", "b", "c", "b", "c", "a"], 2))
