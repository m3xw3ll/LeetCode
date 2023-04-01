def count_points(points, queries):
    out = [0] * len(queries)
    for idx, q in enumerate(queries):
        for p in points:
            radius = q[2]
            circle_x = q[0]
            circle_y = q[1]
            point_x = p[0]
            point_y = p[1]

            square_dist = (circle_x - point_x) + (circle_y - point_y)
            if square_dist <= radius:
                out[idx] += 1
    return out


print(count_points(points=[[1, 3], [3, 3], [5, 3], [2, 2]], queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
