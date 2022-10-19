from collections import Counter


def intersection(nums):
    flat = [x for lst in nums for x in lst]
    c = Counter(flat)
    items = c.items()
    out = [key for key, value in items if value == len(nums)]
    return sorted(out)


print(intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
