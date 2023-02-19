def sort_colors(nums):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        if nums[j] < 1:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > 1:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        else:
            j += 1


print(sort_colors([2, 0, 2, 1, 1, 0]))
