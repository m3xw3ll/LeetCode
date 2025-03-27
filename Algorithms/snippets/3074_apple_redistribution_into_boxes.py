import heapq


def minimum_boxes(apple, capacity):
    apple_sum = sum(apple)
    cnt = 0
    capacity = [-c for c in capacity]
    heapq.heapify(capacity)

    while apple_sum > 0:
        max_capa = heapq.heappop(capacity)
        cnt += 1
        apple_sum -= -max_capa

    return cnt


print(minimum_boxes(apple = [5,5,5], capacity = [2,4,2,7]))