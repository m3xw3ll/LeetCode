import heapq


def minimum_cost(cost):
    cost = [-c for c in cost]
    heapq.heapify(cost)
    out = 0
    while len(cost) >= 3:
        out += heapq.heappop(cost)
        out += heapq.heappop(cost)
        heapq.heappop(cost)
    return -(out + sum(cost))


print(minimum_cost([5, 5]))
