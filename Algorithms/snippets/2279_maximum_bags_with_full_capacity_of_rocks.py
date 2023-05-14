import heapq


def maximum_bags(capacity, rocks, additional_rocks):
    rocks_to_fit = []
    full_bags = 0
    for i in range(len(capacity)):
        heapq.heappush(rocks_to_fit, capacity[i] - rocks[i])

    while rocks_to_fit:
        additional_rocks -= heapq.heappop(rocks_to_fit)
        if additional_rocks >= 0:
            full_bags += 1
    return full_bags


print(maximum_bags(capacity=[2, 3, 4, 5], rocks=[1, 2, 4, 4], additional_rocks=2))
