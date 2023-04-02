import heapq


def k_th_smallest(matrix, k):
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heap.append(matrix[i][j])

    heapq.heapify(heap)
    i = 1
    while i < k:
        heapq.heappop(heap)
        i += 1
    return heap[0]


print(k_th_smallest(matrix=[[-5]], k=1))
