def subsets(nums):
    out = []
    subsets = []

    def backtrack(i):
        if i >= len(nums):
            out.append(subsets.copy())
            return

        subsets.append(nums[i])
        backtrack(i + 1)

        subsets.pop()
        backtrack(i + 1)

    backtrack(0)
    return out


print(subsets([1, 2, 3]))
