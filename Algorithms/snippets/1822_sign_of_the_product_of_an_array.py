def array_sign(nums):
    if 0 in nums:
        return 0
    out = 1
    for n in nums:
        if n < 0:
            out *= -1
    return out


print(array_sign([-1, -2, -3, -4, 3, 2, 1]))
