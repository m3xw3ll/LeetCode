def count_hill_valey(nums):
    cnt = 0
    for i in range(1, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i - 1]
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            cnt += 1
        if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
            cnt += 1
    return cnt


print(count_hill_valey([2, 4, 1, 1, 6, 5]))
