from collections import Counter


def permute_unique(nums):
    def backtrack(out):
        if len(out) == len(nums):
            pems.append(out)
            return
        for key in c:
            if c[key]:
                c[key] -= 1
                backtrack(out + [key])
                c[key] += 1

    pems = []
    c = Counter(nums)
    backtrack([])
    return pems


print(permute_unique([1, 1, 2]))
