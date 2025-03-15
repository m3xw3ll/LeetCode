def transform_array(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i] = 0
        else:
            nums[i] = 1
    return sorted(nums)


print(transform_array([4, 3, 2, 1]))
