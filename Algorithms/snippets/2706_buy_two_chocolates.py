import heapq


def buy_choco(prices, money):
    heapq.heapify(prices)
    costs = heapq.heappop(prices) + heapq.heappop(prices)
    return money - costs if money - costs >= 0 else money


print(buy_choco(prices=[3, 2, 3], money=3))
