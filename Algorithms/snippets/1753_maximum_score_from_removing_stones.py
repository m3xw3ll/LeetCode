import heapq


def maximum_score(a, b, c):
    heap = [-a, -b, -c]
    heapq.heapify(heap)
    cnt = 0
    while True:
        if heap[0] != 0 and heap[1] != 0:
            f = heapq.heappop(heap)
            s = heapq.heappop(heap)
            heapq.heappush(heap, f + 1)
            heapq.heappush(heap, s + 1)
            cnt += 1
        else:
            break
    return cnt


print(maximum_score(a=2, b=4, c=6))
