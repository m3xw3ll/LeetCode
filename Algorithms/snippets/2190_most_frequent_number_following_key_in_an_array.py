from collections import Counter


def most_frequent(nums, key):
    c = Counter()
    for i, v in enumerate(nums):
        if v == key and i + 1 < len(nums):
            c[nums[i + 1]] += 1
    return c.most_common(1)[0][0]


print(most_frequent(nums=[1, 100, 200, 1, 100], key=1))
