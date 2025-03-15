import math


def area_of_max_diagonal(dimensions):
    max_dia = 0
    max_area = 0
    for rect in dimensions:
        d = math.sqrt((rect[0] ** 2) + (rect[1] ** 2))
        if d > max_dia or (d == max_dia and rect[0] * rect[1] > max_area):
            max_area = rect[0] * rect[1]
            max_dia = d
    return max_area


print(area_of_max_diagonal([[6, 5], [8, 6], [2, 10], [8, 1], [9, 2], [3, 5], [3, 5]]))
