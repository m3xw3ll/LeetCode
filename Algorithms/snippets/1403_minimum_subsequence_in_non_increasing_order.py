def min_subsequence(nums):
    if len(nums) == 1: return nums
    if len(set(nums)) == 1: return nums
    nums = sorted(nums, reverse=True)
    for i in range(len(nums)):
        if sum(nums[:i]) > sum(nums[i:]):
            return nums[:i]


print(min_subsequence([6]))
