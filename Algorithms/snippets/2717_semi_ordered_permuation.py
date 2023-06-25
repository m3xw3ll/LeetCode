def semi_orderned_permutation(nums):
    x = nums.index(1)
    y = nums.index(max(nums))
    return x + (len(nums) - y - 1) if x < y else x + (len(nums) - y - 1) - 1


print(semi_orderned_permutation([2, 1, 4, 3]))
