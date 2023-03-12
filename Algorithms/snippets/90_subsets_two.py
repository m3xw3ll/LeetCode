def subsets_with_dup(nums):
    out = set()
    nums = sorted(nums)

    def bt(i, curr):
        out.add(curr)
        for i in range(i, len(nums)):
            bt(i + 1, tuple(list(curr) + [nums[i]]))

    bt(0, tuple())
    return out


print(subsets_with_dup([1, 2, 2]))
