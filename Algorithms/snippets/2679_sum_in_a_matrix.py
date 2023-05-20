def matrix_sum(nums):
    out = 0
    for r in nums:
        r.sort()
    for c in zip(*nums):
        out += max(c)
    return out


print(matrix_sum([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
