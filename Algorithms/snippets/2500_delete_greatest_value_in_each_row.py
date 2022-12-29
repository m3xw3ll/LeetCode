def delete_greatest_value(grid):
    s = 0

    for i in range(len(grid)):
        grid[i].sort(reverse=True)

    for i in range(len(grid[0])):
        max_val = 0
        for j in range(len(grid)):
            max_val = max(max_val, grid[j][i])
        s += max_val
    return s


print(delete_greatest_value([[1, 2, 4], [3, 3, 1]]))
