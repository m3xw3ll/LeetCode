def sum_counts(nums):
    out = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            out += len(set(nums[i:j])) ** 2
    return out


print(sum_counts([1, 2, 1]))
