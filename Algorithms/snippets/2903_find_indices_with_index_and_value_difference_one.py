def find_indices(nums, index_difference, value_difference):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if abs(i-j) >= index_difference and abs(nums[i] - nums[j]) >= value_difference:
                return [i, j]
    return [-1, -1]


print(find_indices(nums=[5, 1, 4, 1], index_difference=2, value_difference=4))
