def maximize_sum(nums, k):
    m = max(nums)
    out = 0
    for i in range(k):
        out += m
        m += 1
    return out


print(maximize_sum(nums=[1, 2, 3, 4, 5], k=3))
