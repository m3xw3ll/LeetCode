def missing_multiple(nums, k):
    i = k
    while True:
        if i not in nums:
            return i
        i += k
    return False


print(missing_multiple(nums = [8,2,3,4,6], k = 2))