from math import floor, sqrt


def pick_gifts(gifts, k):
    i = 1
    while i <= k:
        max_idx = gifts.index(max(gifts))
        gifts[max_idx] = floor(sqrt(gifts[max_idx]))
        i += 1
    return sum(gifts)


print(pick_gifts(gifts=[25, 64, 9, 4, 100], k=4))
