import heapq
from collections import Counter


def max_subsequence(nums, k):
    heap = list()
    out = list()
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    cnt = Counter(heap)
    for n in nums:
        if cnt[n] > 0:
            cnt[n] -= 1
            out.append(n)
    return out


print(max_subsequence(nums=[2, 1, 3, 3], k=2))
