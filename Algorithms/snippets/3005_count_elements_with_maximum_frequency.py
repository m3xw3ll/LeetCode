from collections import Counter


def max_fequency_elements(nums):
    c = Counter(nums)
    max_count = max(c.values())
    return sum(count for count in c.values() if count == max_count)


print(max_fequency_elements([1, 2, 2, 3, 1, 4]))
