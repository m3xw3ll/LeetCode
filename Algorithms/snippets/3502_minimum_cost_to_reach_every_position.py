def min_costs(cost):
    min_prefix = [cost[0]]
    for i in range(1, len(cost)):
        min_prefix.append(min(min_prefix[-1], cost[i]))
    return min_prefix


print(min_costs([5, 3, 4, 1, 3, 2]))
