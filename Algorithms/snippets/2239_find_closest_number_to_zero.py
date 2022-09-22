def find_closest_number(nums):
    closest = nums[0]

    for num in nums:
        if abs(num) == abs(closest) and num > closest:
            closest = num
        elif abs(num) < abs(closest):
            closest = num
    return closest


print(find_closest_number([-4, -2, 1, 4, 8]))
