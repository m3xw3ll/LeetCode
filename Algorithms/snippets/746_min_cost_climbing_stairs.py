def min_cost_climbing_stairs(cost):
    cost.append(0)
    for i in range(len(cost) -3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])


print(min_cost_climbing_stairs([10, 15, 20]))