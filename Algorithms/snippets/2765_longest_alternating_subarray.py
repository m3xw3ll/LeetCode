def alternating_subarray(nums):
    out = -1
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] == 1:
            l = 2
            for j in range(i + 2, len(nums)):
                if j < len(nums) and nums[j] == nums[j - 2]:
                    l += 1
                else:
                    break
            out = max(l, out)
    return -1 if out == 0 else out


print(alternating_subarray([2, 3, 4, 3, 4]))
