def single_non_duplicate(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = left + right // 2
        if middle % 2 == 1:
            middle -= 1
        if nums[middle] != nums[middle + 1]:
            right = middle
        else:
            left = middle + 2
    return nums[left]


print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
