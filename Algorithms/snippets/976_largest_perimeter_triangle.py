def largest_perimeter(nums):
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return sum(nums[i:i+3])
    return 0


print(largest_perimeter([2, 1, 2]))
