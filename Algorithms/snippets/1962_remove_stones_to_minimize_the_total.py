import heapq


def min_stone_sum(piles, k):
    heap = []
    i = 1
    for p in range(len(piles)):
        heapq.heappush(heap, -piles[p])
    while i <= k:
        tmp = heapq.heappop(heap)
        heapq.heappush(heap, tmp // 2)
        i += 1
    return -sum(heap)


print(min_stone_sum(piles=[5, 4, 9], k=2))
