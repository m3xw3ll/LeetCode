def find_max_average(nums, k):
    tmp = sum(nums[:k])
    out = tmp
    for i in range(len(nums) - k):
        tmp = tmp - nums[i] + nums[i+k]
        out = max(out, tmp)
    return out / k


print(find_max_average(nums=[0, 1, 1, 3, 3], k=4))
