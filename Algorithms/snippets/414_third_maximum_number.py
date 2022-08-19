def third_max(nums):
    nums = set(nums)
    if len(nums) <= 2:
        return max(nums)
    idx = 1
    while idx < 3:
        nums.remove(max(nums))
        idx += 1
    return max(nums)


print(third_max([1, 2]))
