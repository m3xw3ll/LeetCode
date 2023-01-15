import math
import heapq


def k_closest(points, k):
    out = list()
    for x, y in points:
        dist = math.sqrt(x ** 2 + y ** 2)
        if len(out) < k:
            heapq.heappush(out, (-dist, [x, y]))
        else:
            heapq.heappushpop(out, (-dist, [x, y]))
    return [out[i][1] for i in range(k)]


print(k_closest(points=[[1, 3], [-2, 2]], k=1))
