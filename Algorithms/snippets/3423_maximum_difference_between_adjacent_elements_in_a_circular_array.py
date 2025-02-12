def max_adjacent_distance(nums):
    edgecase = abs(nums[0] - nums[len(nums) - 1])
    ret = 0
    for i in range(0, len(nums) - 1):
        ret = max(ret, abs(nums[i] - nums[i+1]))
    return max(ret, edgecase)


print(max_adjacent_distance([-4,-2,-3]))