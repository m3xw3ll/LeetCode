def distinct_difference_array(nums):
    out = []
    for n in range(len(nums)):
        prefix = set(nums[0:n+1])
        suffix = set(nums[n+1:])
        print(prefix, suffix)
        out.append(len(prefix) - len(suffix))
    return out


print(distinct_difference_array([3, 2, 3, 4, 2]))
