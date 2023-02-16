def max_profit(prices):
    out = 0
    buy_pointer = 0
    sell_pointer = 1
    l = len(prices)

    while sell_pointer < l:
        if prices[buy_pointer] < prices[sell_pointer]:
            out = max(out, prices[sell_pointer] - prices[buy_pointer])
        else:
            buy_pointer = sell_pointer
        sell_pointer += 1
    return out


print(max_profit([7, 1, 5, 3, 6, 4]))
