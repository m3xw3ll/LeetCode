def target_indices(nums, target):
    nums = sorted(nums)
    out = [i for i, x in enumerate(nums) if x == target]
    return out


print(target_indices([1, 2, 5, 2, 3], 2))