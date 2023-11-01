def minimum_sum(nums):
    out = float('inf')
    flag = False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] < nums[j] and nums[k] < nums[j]:
                    out = min(out, sum([nums[i], nums[j], nums[k]]))
                    flag = True
    return -1 if not flag else out


print(minimum_sum([5, 4, 8, 7, 10, 2]))
