def surface_area(grid):
    out = 0
    n = len(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                out += (grid[i][j] * 4) + 2
            if i:
                out -= min(grid[i][j], grid[i - 1][j]) * 2
            if j:
                out -= min(grid[i][j], grid[i][j - 1]) * 2
    return out


print(surface_area([[1, 2], [3, 4]]))
