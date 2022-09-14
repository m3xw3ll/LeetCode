from collections import Counter

def find_duplicate(nums):
    n = Counter(nums)
    for i in n:
        if n[i] > 1:
            return i


print(find_duplicate([1, 3, 4, 2, 2]))