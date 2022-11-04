def remove_element(nums, val):
    while val in nums:
        nums.remove(val)
    return nums

print(remove_element(nums=[3, 2, 2, 3], val=3))
