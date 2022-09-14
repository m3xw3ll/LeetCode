def remove_duplicates(nums):
    n = len(nums)
    l = 1

    for i in range(1, n):
        if nums[l-1] == nums[i]:
            continue
        nums[l] = nums[i]
        l += 1

    return l


print(remove_duplicates([1, 1, 2]))