def largest_triangle_area(points):
    out = 0
    l = len(points)

    for i in range(l):
        x1, y1 = points[i]
        for j in range(i+1, l):
            x2, y2 = points[j]
            for k in range(j+1, l):
                x3, y3 = points[k]
                out = max(out, abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))))
    return out


print(largest_triangle_area([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
