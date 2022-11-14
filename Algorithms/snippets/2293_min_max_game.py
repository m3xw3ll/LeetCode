def min_max_game(nums):
    if len(nums) == 1:
        return nums[0]

    while len(nums) != 1:
        new_nums = [-1] * (len(nums) // 2)
        for i in range(0, len(nums) // 2):
            if i % 2 == 0:
                new_nums[i] = min(nums[2 * i], nums[(2 * i) + 1])
            else:
                new_nums[i] = max(nums[2 * i], nums[2 * i + 1])
        nums = new_nums
    return nums[0]


print(min_max_game([1, 3, 5, 2, 4, 8, 2, 2]))
