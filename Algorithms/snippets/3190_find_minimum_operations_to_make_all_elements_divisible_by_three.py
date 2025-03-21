def minimum_operations(nums):
    out = 0
    for i in nums:
        if i % 3 != 0:
            out += 1
    return out


print(minimum_operations([1, 2, 3, 4]))
