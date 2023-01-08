def max_ice_cream(costs, coins):
    costs = sorted(costs)
    cnt = 0

    for c in costs:
        if c <= coins:
            coins -= c
            cnt += 1
        else:
            break
    return cnt


print(max_ice_cream(costs=[1, 3, 2, 4, 1], coins=7))
