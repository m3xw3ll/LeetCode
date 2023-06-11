def find_non_min_or_max(nums):
    nums = sorted(nums)
    return -1 if len(nums) <= 2 else nums[1]


print(find_non_min_or_max([1, 2]))
