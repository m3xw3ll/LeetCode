def maximum_wealth(accounts):
    return max([sum(i) for i in accounts])


print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
