from collections import defaultdict


def find_lonely(nums):
    dic = defaultdict(int)
    out = []
    for num in nums:
        dic[num] += 1

    for num in nums:
        if dic[num-1] or dic[num+1] or dic[num] > 1:
            continue
        out.append(num)

    return out


print(find_lonely([10, 6, 5, 8]))
