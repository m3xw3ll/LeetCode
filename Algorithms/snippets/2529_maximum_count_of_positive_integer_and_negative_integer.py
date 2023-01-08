import bisect


def maximum_count(nums):
    left = bisect.bisect_left(nums, 0)
    right = len(nums) - bisect.bisect_right(nums, 0)
    return max(left, right)


print(maximum_count([-3, -2, -1, 0, 0, 1, 2]))
