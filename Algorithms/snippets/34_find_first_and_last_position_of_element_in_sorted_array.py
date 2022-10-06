def search_range(nums, target):
    if target in nums:
        p1 = nums.index(target)
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == target:
                p2 = i
                break
        return [p1, p2]
    return [-1, -1]


print(search_range([5, 7, 7, 8, 8, 10], 8))
