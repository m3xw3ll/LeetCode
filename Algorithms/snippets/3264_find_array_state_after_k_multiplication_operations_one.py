import heapq


def get_final_state(nums, k, multiplier):
    h = list(zip(nums, range(len(nums))))
    heapq.heapify(h)
    while k:
        n, idx = heapq.heappop(h)
        heapq.heappush(h, (n * multiplier, idx))
        k -= 1
    return [x[0] for x in sorted(h, key=lambda t: t[1])]



print(get_final_state([2, 1, 3, 5, 6], k=5, multiplier=2))
