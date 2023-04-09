def find_score(nums):
    mark = [0] * (len(nums) + 1)
    out = 0

    for i, j in sorted([val, idx] for idx, val in enumerate(nums)):
        if not mark[j]:
            out += i
            mark[j] = 1
            mark[j-1] = 1
            mark[j+1] = 1
    return out


print(find_score([2, 1, 3, 4, 5, 2]))
