def running_sum(nums):
    out = []
    runsum = nums[0]
    out.append(runsum)
    for i in range(1, len(nums)):
        out.append(runsum + nums[i])
        runsum += nums[i]

    return out


print(running_sum([1, 2, 3, 4]))
