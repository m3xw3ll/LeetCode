def triangular_sum(nums):
    for i in range(len(nums), 0, -1):
        for j in range(1, i):
            nums[j - 1] += nums[j]
            nums[j - 1] %= 10
    return nums[0]


print(triangular_sum([1, 2, 3, 4, 5]))
