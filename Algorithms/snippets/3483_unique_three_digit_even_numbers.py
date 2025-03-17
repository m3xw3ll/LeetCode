from itertools import permutations


def total_numbers(digits):
    candidates = set()
    for d1, d2, d3 in permutations(digits, 3):
        if d1 != 0 and d3 % 2 == 0:
            candidates.add((d1, d2, d3))
    return len(candidates)


print(total_numbers([1, 2, 3, 4]))
