def count_points(rings):
    cnt = 0
    for i in range(0, 10):
        if rings.count('R' + str(i)) and rings.count('B' + str(i)) and rings.count('G' + str(i)):
            cnt += 1
    return cnt


print(count_points('B0B6G0R6R0R6G9'))
