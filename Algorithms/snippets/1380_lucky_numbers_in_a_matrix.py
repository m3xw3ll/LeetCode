def lucky_numbers(matrix):
    row_mins = set()
    col_maxs = set()

    for row in matrix:
        row_mins.add(min(row))

    for col in zip(*matrix):
        col_maxs.add(max(col))

    return list(row_mins.intersection(col_maxs))


print(lucky_numbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
