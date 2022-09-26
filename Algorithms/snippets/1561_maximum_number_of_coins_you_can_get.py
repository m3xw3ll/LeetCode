def max_coins(piles):
    coins = 0
    piles = sorted(piles, reverse=True)

    for i in range(1, len(piles) * 2 // 3, 2):
        coins += piles[i]
    return coins


print(max_coins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
