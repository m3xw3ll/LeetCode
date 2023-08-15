def max_sum(nums):
    out = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            n1 = [int(x) for x in str(nums[i])]
            n2 = [int(x) for x in str(nums[j])]
            if max(n1) == max(n2) and nums[i] + nums[j] > out:
                out = nums[i] + nums[j]
    return out


print(max_sum([51, 71, 17, 24, 42]))
