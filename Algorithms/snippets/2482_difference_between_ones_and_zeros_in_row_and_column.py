def ones_minus_zeros(grid):
    rows = [sum(r) for r in grid]
    cols = [sum(c) for c in zip(*grid)]

    out = [[0] * len(grid) for _ in range(len(grid[0]))]

    for i in range(len(out)):
        for j in range(len(out[0])):
            out[i][j] = 2 * rows[i] + 2 * cols[j] - len(grid) - len(grid[0])
    return out


print(ones_minus_zeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
