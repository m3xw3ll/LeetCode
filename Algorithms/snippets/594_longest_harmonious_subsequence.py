from collections import defaultdict


def find_lhs(nums):
    dic = defaultdict(int)
    out = 0
    for n in nums:
        dic[n] += 1

    for k in dic.keys():
        if dic.get(k+1):
            out = max(out, dic[k] + dic[k+1])
    return out


print(find_lhs([1, 3, 2, 2, 5, 2, 3, 7]))
