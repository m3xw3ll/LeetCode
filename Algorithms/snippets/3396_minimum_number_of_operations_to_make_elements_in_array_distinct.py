def minimum_operations(nums):
    if len(nums) == len(set(nums)):
        return 0

    cnt = 0
    while len(nums) >= 3:
        nums = nums[3:]
        cnt += 1
        if len(nums) == len(set(nums)):
            return cnt

    return cnt + 1


print(minimum_operations([4,5,6,4,4]))
