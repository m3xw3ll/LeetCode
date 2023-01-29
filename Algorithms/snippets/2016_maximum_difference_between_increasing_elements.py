def maximum_difference(nums):
    out = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            out = max(out, nums[j] - nums[i])
    return -1 if out == 0 else out


print(maximum_difference([1, 5, 2, 10]))
