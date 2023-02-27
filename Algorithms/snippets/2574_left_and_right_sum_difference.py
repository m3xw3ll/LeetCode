def left_right_difference(nums):
    left = 0
    right = sum(nums)

    for idx, num in enumerate(nums):
        left += num
        nums[idx] = abs(left-right)
        right -= num
    return nums


print(left_right_difference([10, 4, 8, 3]))
