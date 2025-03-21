import heapq


def minimum_average(nums):
    out = list()
    min_heap = nums
    heapq.heapify(min_heap)
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)

    for i in range(len(nums) // 2):
        out.append((heapq.heappop(min_heap) + (-1 * heapq.heappop(max_heap))) / 2)
    return min(out)


print(minimum_average([7, 8, 3, 4, 15, 13, 4, 1]))
