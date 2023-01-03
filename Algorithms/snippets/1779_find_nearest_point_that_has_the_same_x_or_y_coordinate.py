def nearest_valid_points(x, y, points):
    nearest = float('inf')
    out = -1
    for idx, (px, py) in enumerate(points):
        dx = x - px
        dy = y - py
        if abs(dx + dy) < nearest and dx * dy == 0:
            nearest = abs(dx + dy)
            out = idx
    return out


print(nearest_valid_points(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
