def final_prices(prices):
    stack = list()
    for idx, val in enumerate(prices):
        while stack and prices[stack[-1]] >= val:
            prices[stack.pop()] -= val
        stack.append(idx)
    return prices


print(final_prices([8, 4, 6, 2, 3]))
