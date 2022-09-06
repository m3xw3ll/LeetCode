def search_insert(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        if target < nums[middle]:
            right = middle -1
        else:
            left = middle + 1

    return left


print(search_insert([1, 3, 5, 6], 5))