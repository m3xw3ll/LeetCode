def projection_area(grid):
    xy = sum(v > 0 for row in grid for v in row)
    xz = sum([max(i) for i in grid])
    yz = sum([max(i) for i in zip(*grid)])
    return sum([xy, xz, yz])


print(projection_area([[2]]))
