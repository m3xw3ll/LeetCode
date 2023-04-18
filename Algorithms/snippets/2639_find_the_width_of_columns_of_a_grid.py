def find_column_width(grid):
    grid = list(zip(*grid))
    out = [0] * len(grid)
    for idx, r in enumerate(grid):
        l = 0
        for v in r:
            l = max(l, len(str(v)))
        out[idx] = l
    return out


print(find_column_width([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))
