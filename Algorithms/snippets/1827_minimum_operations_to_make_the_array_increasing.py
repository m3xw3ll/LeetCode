def min_operations(nums):
    out = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            out += nums[i-1] - nums[i] + 1
            nums[i] = nums[i-1] + 1
    return out


print(min_operations([1, 5, 2, 4, 1]))