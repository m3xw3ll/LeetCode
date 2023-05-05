from collections import Counter


def minimum_rounds(tasks):
    c = Counter(tasks)
    rounds = 0

    for n in c.values():
        if n == 1:
            return - 1
        rounds += n // 3
        if n % 3:
            rounds += 1
    return rounds


print(minimum_rounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
