from collections import Counter


def equal_pairs(grid):
    trans = Counter(zip(*grid))
    grid = Counter(map(tuple, grid))
    print(grid)
    print(trans)
    return sum(trans[t] * grid[t] for t in trans)


print(equal_pairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
