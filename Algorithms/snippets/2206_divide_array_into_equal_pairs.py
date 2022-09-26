def divide_array(nums):
    lookup = dict()
    for num in nums:
        if num in lookup:
            lookup[num] += 1
        else:
            lookup[num] = 1

    for occ in lookup.values():
        if occ % 2 != 0:
            return False
    return True


print(divide_array([3, 2, 3, 2, 2, 2]))
