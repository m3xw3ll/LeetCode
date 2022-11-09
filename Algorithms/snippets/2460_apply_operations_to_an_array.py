def apply_operations(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    nonzero = [x for x in nums if x != 0]
    zeroes = [y for y in nums if y == 0]

    return nonzero + zeroes


print(apply_operations([1, 2, 2, 1, 1, 0]))
