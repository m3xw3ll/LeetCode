def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    l = []
    for i in range(len(nums)):
        m = nums[i]
        rem = nums[:i] + nums[i+1:]

        for p in permute(rem):
            l.append([m] + p)
    return l


print(permute([1,2,3]))