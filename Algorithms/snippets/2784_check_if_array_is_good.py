def is_good(nums):
    n = len(nums)
    return list(range(1, n)) + [n - 1] == sorted(nums)


print(is_good([1, 3, 3, 2]))