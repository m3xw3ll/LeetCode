def max_sum(grid):
    hourglass_offset = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
    s = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows - 2):
        for j in range(cols - 2):
            s = max(s, sum(grid[i+x][j+y] for x, y in hourglass_offset))
    return s


print(max_sum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]))
