def min_operations(nums, k):
    target = set([i + 1 for i in range(k)])
    tmp = set()
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in target:
            tmp.add(nums[i])
        if sorted(tmp) == sorted(target):
            return len(nums) - i


print(min_operations(nums=[3, 1, 5, 4, 2], k=5))
