def max_ascending_sum(nums):
    out = 0
    s = 0
    for i in range(len(nums)):
        if i == 0 or nums[i-1] < nums[i]:
            s += nums[i]
        else:
            s = nums[i]
        out = max(out, s)
    return out


print(max_ascending_sum([10, 20, 30, 5, 10, 50]))
