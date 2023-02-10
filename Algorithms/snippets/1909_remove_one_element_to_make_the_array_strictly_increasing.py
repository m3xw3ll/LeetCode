def can_be_increasing(nums):
    for i in range(len(nums)):
        if nums[:i] + nums[i+1:] == sorted(list(set(nums[:i] + nums[i+1:]))):
            return True
    return False


print(can_be_increasing([1, 1, 1]))
