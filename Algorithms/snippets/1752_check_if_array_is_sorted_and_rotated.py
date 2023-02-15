def check(nums):
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > prev:
            prev = nums[i]
        else:
            return nums[i:] + nums[:i] == sorted(nums)
    return True


print(check([2, 1, 3, 4]))