from collections import Counter


def single_number(nums):
    c = Counter(nums)
    for i, j in c.items():
        if j == 1:
            return i


print(single_number([2, 2, 1]))