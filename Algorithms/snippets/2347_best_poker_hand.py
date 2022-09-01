from collections import Counter


def best_hand(ranks, suits):
    suits = Counter(set(suits))
    ranks = Counter(ranks)
    if len(suits) == 1:
        return 'Flush'
    elif max(ranks.values()) >= 3:
        return 'Three of a Kind'
    elif max(ranks.values()) == 2:
        return 'Pair'
    else:
        return 'High Card'


print(best_hand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]))
