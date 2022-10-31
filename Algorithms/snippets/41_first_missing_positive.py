def first_missing_positive(nums):
    nums = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i


print(first_missing_positive([3, 4, -1, 1]))
