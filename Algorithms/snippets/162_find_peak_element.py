def find_peak_element(nums):
    left = 0
    right = len(nums) - 1
    if len(nums) == 1:
        return 0
    if nums[-1] > nums[-2]:
        return right

    while left <= right:
        middle = (left + right) // 2
        if (nums[middle] > nums[middle-1]) and (nums[middle] > nums[middle+1]):
            return middle
        if nums[middle-1] > nums[middle]:
            right = middle -1
        else:
            left = middle +1
    return -1



print(find_peak_element([1, 2, 3, 1]))