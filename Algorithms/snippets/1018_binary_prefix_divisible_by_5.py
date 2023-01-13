def prefix_div_by_five(nums):
    out = list()
    num = 0
    for n in nums:
        num = (num * 2 + n) % 5
        out.append(num == 0)
    return out


print(prefix_div_by_five([0, 1, 1]))
