from collections import defaultdict


def contains_nearby_duplicates(nums, k):
    dic = defaultdict()
    for idx, num in enumerate(nums):
        if num in dic and idx - dic[num] <= k:
            return True
        dic[num] = idx
    return False


print(contains_nearby_duplicates([1, 2, 3, 1], 3))
