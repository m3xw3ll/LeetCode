def largest_local(grid):
    n = len(grid)
    matrix = [[1] * (n - 2) for i in range(n - 2)]

    for i in range(0, n-2):
        for j in range(0, n-2):
            maxx = 0
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    maxx = max(maxx, grid[row][col])
            matrix[i][j] = maxx
    return matrix


print(largest_local([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
