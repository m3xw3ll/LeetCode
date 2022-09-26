def is_monotonic(nums):
    return True if nums == sorted(nums) or nums == sorted(nums, reverse=True) else False


print(is_monotonic([6, 5, 4, 4]))
