def check_straight_line(coordinates):
    (x1, y1) = coordinates[0]
    (x2, y2) = coordinates[1]

    for (x3, y3) in coordinates[2:]:
        if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
            return False
    return True


print(check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
