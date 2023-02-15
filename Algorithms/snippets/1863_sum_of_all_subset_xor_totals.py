def powerset(s):
    sets = [[]]
    for i in s:
        newsets = []
        for k in sets:
            newsets.append(k + [i])
        sets += newsets
    return sets


def subset_xor_sum(nums):
    sets = powerset(nums)
    out = 0
    for i in sets:
        tmp = 0
        for j in i:
            tmp ^= j
        out += tmp
    return out


print(subset_xor_sum([5, 1, 6]))
