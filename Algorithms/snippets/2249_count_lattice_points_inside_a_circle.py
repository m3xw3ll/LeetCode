import math


def is_point_in_circle(x, y, r, square_x, square_y):
    return math.sqrt((square_x - x) ** 2 + (square_y - y) ** 2) <= r


def count_lattice_points(circles):
    points = set()
    for cx, cy, cr in circles:
        for px in range(cx - cr, cx + cr + 1):
            for py in range(cy - cr, cy + cr + 1):
                if (px, py) not in points and is_point_in_circle(cx, cy, cr, px, py):
                    points.add((px, py))
    return len(points)


print(count_lattice_points([[2, 2, 2], [3, 4, 1]]))
