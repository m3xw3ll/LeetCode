from itertools import accumulate


def min_start_value(nums):
    psum = list(accumulate(nums))
    return max(1, 1 - min(psum))


print(min_start_value([-3, 2, -3, 4, 2]))
