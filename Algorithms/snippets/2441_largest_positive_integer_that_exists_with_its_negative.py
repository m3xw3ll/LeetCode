def find_max_k(nums):
    nums = set(nums)
    out = []
    for num in nums:
        if -num in nums:
            out.append(num)

    if len(out) > 0:
        return max(out)
    else:
        return -1


print(find_max_k([-10, 8, 6, 7, -2, -3]))
