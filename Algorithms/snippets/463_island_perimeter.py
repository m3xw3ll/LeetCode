def island_perimeter(grid):
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                p += 4
                if i >= 1 and grid[i-1][j] == 1:
                    p -= 2
                if j >= 1 and grid[i][j-1] == 1:
                    p -= 2
    return p


print(island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
