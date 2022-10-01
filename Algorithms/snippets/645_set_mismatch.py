def find_error_nums(nums):
    n = len(nums)
    s = n * (n + 1) // 2
    missing = s - sum(set(nums))
    dup = sum(nums) + missing - s
    return [dup, missing]


print(find_error_nums([1, 2, 2, 4]))
