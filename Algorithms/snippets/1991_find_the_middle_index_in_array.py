def find_middle_index(nums):
    sum_left = 0
    sum_right = sum(nums)
    for i, n in enumerate(nums):
        sum_left += n
        if sum_left == sum_right:
            return i
        sum_right -= n
    return -1


print(find_middle_index([2, 3, -1, 8, 4]))