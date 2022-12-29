def pivot_index(nums):
    n = len(nums)
    for i in range(n):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1


print(pivot_index([1, 7, 3, 6, 5, 6]))
