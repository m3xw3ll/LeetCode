from collections import Counter


def find_winners(matches):
    winners = []
    loosers = []

    for i in range(len(matches)):
        winners.append(matches[i][0])
        loosers.append(matches[i][1])

    c = Counter(loosers)
    final_winners = list(set(winners) - set(c.keys()))
    final_loosers = []

    for k, v in c.items():
        if v == 1:
            final_loosers.append(k)
    return [sorted(final_winners), sorted(final_loosers)]


print(find_winners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
