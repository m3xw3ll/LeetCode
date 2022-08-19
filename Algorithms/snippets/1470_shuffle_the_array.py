def shuffle(nums, n):
    left = nums[0:n]
    right = nums[n:]
    out = []
    for i in range(len(left)):
        out.append(left[i])
        out.append(right[i])
    return out


print(shuffle([2, 5, 1, 3, 4, 7, ], 3))