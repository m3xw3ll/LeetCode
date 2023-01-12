def rearrange_array(nums):
    n = len(nums)
    pos = list()
    neg = list()
    out = list()
    for i in range(n):
        if nums[i] < 0:
            neg.append(nums[i])
        else:
            pos.append(nums[i])

    neg = neg[::-1]
    pos = pos[::-1]

    for i in range(n):
        if i % 2 == 0:
            out.append(pos.pop())
        else:
            out.append(neg.pop())
    return out


print(rearrange_array([3, 1, -2, -5, 2, -4]))
