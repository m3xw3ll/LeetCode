def minimum_operations(nums):
    nums = [num for num in nums if num != 0]
    return len(set(nums))


print(minimum_operations([1, 5, 0, 3, 5]))