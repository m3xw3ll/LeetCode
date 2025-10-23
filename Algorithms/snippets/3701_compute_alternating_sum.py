def alternating_sum(nums):
    r = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            r += nums[i]
        else:
            r -= nums[i]
    return r


print(alternating_sum([1,3,5,7]))