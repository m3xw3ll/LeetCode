def max_width_of_vertical_area(points):
    cnt = 0
    points = sorted(points)

    for i in range(len(points) - 1):
        cnt = max(cnt, points[i+1][0] - points[i][0])
    return cnt


print(max_width_of_vertical_area([[8, 7], [9, 9], [7, 4], [9, 7]]))
