def count_pairs(nums, target):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                cnt += 1
    return cnt


print(count_pairs(nums=[-1, 1, 2, 3, 1], target=2))
