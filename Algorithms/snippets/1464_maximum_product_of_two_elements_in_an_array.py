def max_product(nums):
    nums = sorted(nums)
    return (nums[-2] -1 ) * (nums[-1] - 1)


print(max_product([3, 4, 5, 2]))