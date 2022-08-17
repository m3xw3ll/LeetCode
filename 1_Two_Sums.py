def two_sums(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        rem = target - nums[i]
        if rem in seen:
            return [i, seen[rem]]
        seen[value] = i


print(two_sums([2, 7, 11, 15], 9))