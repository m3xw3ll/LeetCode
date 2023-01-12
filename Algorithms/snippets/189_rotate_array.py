def rotate(nums, k):
    if len(nums) == 0:
        return nums
    k = k % len(nums)
    nums[:len(nums)-k], nums[len(nums)-k:] = nums[len(nums)-k:], nums[:len(nums)-k]


print(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
