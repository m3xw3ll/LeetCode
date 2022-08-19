from collections import Counter


def majority_element(nums):
    c = Counter(nums)
    l = len(nums)
    for i, j in c.items():
        if j >= len(nums) / 2:
            return i


print(majority_element([2,2,1,1,1,2,2]))