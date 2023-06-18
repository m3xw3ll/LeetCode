def find_value_of_partition(nums):
    nums = sorted(nums)
    return min(nums[i+1] - nums[i] for i in range(len(nums) - 1))


print(find_value_of_partition([84, 11, 100, 100, 75]))
