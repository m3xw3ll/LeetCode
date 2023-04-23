from collections import Counter


def find_matrix(nums):
    c = Counter(nums)
    m = max(c.values())
    out = list(c.elements())
    return [out[i::m] for i in range(m)]


print(find_matrix([1, 3, 4, 1, 2, 3, 1]))
