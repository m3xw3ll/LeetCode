def valid_square(p1, p2, p3, p4):
    def dist(point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

    D = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]
    D.sort()
    return 0 < D[0] == D[1] == D[2] == D[3] and D[4] == D[5]


print(valid_square(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))
