def min_cost_to_move_chips(position):
    odds = 0
    evens = 0

    for p in position:
        if p % 2 == 0:
            evens += 1
        else:
            odds += 1
    return min(odds, evens)


print(min_cost_to_move_chips([1, 2, 3]))