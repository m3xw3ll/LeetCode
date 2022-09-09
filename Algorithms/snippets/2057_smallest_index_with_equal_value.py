def smallest_equal(nums):
    indicies = []
    for idx, num in enumerate(nums):
        if idx % 10 == num:
            indicies.append(idx)
    if indicies:
        return min(indicies)
    else:
        return -1


print(smallest_equal([4, 3, 2, 1]))
