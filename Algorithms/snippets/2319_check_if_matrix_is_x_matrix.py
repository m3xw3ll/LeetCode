def check_xmatrix(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i -1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True


print(check_xmatrix(grid=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
