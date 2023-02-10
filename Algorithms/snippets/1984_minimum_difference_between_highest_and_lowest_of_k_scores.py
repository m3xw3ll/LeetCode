def minimum_difference(nums, k):
    out = 100000
    nums = sorted(nums)
    for i in range(len(nums) - k + 1):
        tmp = nums[i:i+k]
        out = min(out, tmp[-1] - tmp[0])
    return out


print(minimum_difference(nums=[9, 4, 1, 7], k=2))
