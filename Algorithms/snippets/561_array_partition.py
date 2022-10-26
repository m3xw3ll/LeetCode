def array_pair_sum(nums):
    out = 0
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        out += min((nums[i], nums[i]+1))
    return out


print(array_pair_sum([1, 4, 3, 2]))