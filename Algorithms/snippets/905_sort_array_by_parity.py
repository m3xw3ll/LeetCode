def sort_array_by_parity(nums):
    out = []
    for x in nums:
        if x % 2 == 0:
            out.append(x)
    for y in nums:
        if y % 2 != 0:
            out.append(y)
    return out


print(sort_array_by_parity([3, 1, 2, 4]))