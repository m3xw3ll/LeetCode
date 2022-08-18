def maximum_product(nums):
    nums = sorted(nums)
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


print(maximum_product([1, 2, 3]))