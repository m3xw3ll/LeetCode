def all_cells_dist_order(rows, cols, rcenter, ccenter):
    out = [[x, y] for y in range(cols) for x in range(rows)]
    out.sort(key=lambda x: abs(x[0] - rcenter) + abs(x[1] - ccenter))
    return out


print(all_cells_dist_order(2, 3, 1, 2))