def is_array_special(nums):
    for i in range(len(nums) - 1):
        if nums[i] % 2 == nums[i+1] % 2:
            return False
    return True


print(is_array_special([4,3,1,6]))
