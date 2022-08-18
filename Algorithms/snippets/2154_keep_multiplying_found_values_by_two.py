def find_final_value(nums, original):
    if original not in nums:
        return original
    else:
        dropped = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if nums[i] != original:
                dropped.append(nums[i])
            else:
                original *= 2
    return original


print(find_final_value([5, 3, 6, 1, 12], 3))