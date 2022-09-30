from collections import defaultdict


def count_difference(nums, k):
    seen = defaultdict(int)
    cnt = 0
    for num in nums:
        tmp1 = num - k
        tmp2 = num + k
        if tmp1 in seen:
            cnt += seen[tmp1]
        if tmp2 in seen:
            cnt += seen[tmp2]
        seen[num] += 1
    return cnt


print(count_difference([1, 2, 2, 1], 1))
