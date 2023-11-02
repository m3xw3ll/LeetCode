from collections import Counter
import heapq


def min_length_after_removals(nums):
    cnt = [-x for x in Counter(nums).values()]
    heapq.heapify(cnt)
    while len(cnt) > 1:
        first = -heapq.heappop(cnt)
        second = -heapq.heappop(cnt)
        if first > 1:
            heapq.heappush(cnt, -first + 1)
        if second > 1:
            heapq.heappush(cnt, -second + 1)
    return -sum(cnt)


print(min_length_after_removals([1, 1, 2]))
