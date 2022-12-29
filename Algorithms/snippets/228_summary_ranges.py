def summary_ranges(nums):
    begin = 0
    res = []
    for i in range(len(nums)):
        if i + 1 >= len(nums) or nums[i+1] - nums[i] != 1:
            b = str(nums[begin])
            e = str(nums[i])
            res.append(b + '->' + e if b != e else e)
            begin = i + 1
    return res


print(summary_ranges([0, 1, 2, 4, 5, 7]))
