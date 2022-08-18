from collections import Counter


def find_duplicates(nums):
    c = Counter(nums)
    return [key for key, val in c.items() if val == 2]


print(find_duplicates([4,3,2,7,8,2,3,1]))