def missing_number(nums):
    length = len(nums)
    return length * (length + 1) // 2 - sum(nums)


print(missing_number([3, 0, 1]))