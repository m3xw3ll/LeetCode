def find_max_fish(grid):
    rows = len(grid)
    cols = len(grid[0])
    visit = [[False] * cols for r in range(rows)]
    out = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0 or visit[i][j]:
            return 0
        visit[i][j] = True
        return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + grid[i][j]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] and not visit[i][j]:
                out = max(out, dfs(i, j))
    return out


print(find_max_fish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
