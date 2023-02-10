def build_array(nums):
    out = [0] * len(nums)
    for i in range(len(nums)):
        out[i] = nums[nums[i]]
    return out


print(build_array([0, 2, 1, 5, 3, 4]))
