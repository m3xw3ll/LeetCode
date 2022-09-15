def is_boomerang(points):
    x1, x2, x3 = points[0][0], points[1][0], points[2][0]
    y1, y2, y3 = points[0][1], points[1][1], points[2][1]

    a = (x1 * (y2 - y3) +
         x2 * (y3 - y1) +
         x3 * (y1 - y2))

    return False if a == 0 else True


print(is_boomerang([[1, 1], [2, 3], [3, 2]]))
