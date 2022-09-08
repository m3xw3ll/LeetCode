def contains_duplicates(nums):
    s = set(nums)
    if len(nums) == len(s):
        return False
    return True


print(contains_duplicates([1, 2, 3, 4]))