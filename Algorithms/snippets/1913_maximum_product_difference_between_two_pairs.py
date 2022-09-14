def max_product_difference(nums):
    nums = sorted(nums)
    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


print(max_product_difference([5, 6, 2, 7, 4]))
