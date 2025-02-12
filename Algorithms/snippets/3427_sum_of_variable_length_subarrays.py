def subarray_sum(nums):
    ret = 0
    for i in range(len(nums)):
        start = max(0, i - nums[i])
        ret += sum(nums[start:i + 1])
    return ret


print(subarray_sum([2,3,1]))