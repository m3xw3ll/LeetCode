def min_time_to_visit_all_points(points):
    time = 0
    for i in range(len(points) - 1):
        current = points[i]
        next = points[i + 1]
        time += max(abs(current[0] - next[0]), abs(current[1] - next[1]))
    return time


print(min_time_to_visit_all_points([[1, 1], [3, 4], [-1, 0]]))
