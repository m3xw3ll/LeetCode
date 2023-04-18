def reduction_operations(nums):
    ans = val = 0
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            val += 1
        ans += val
    return ans


print(reduction_operations([1, 1, 2, 2, 3]))
