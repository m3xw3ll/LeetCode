def set_zeroes(matrix):
    if not matrix:
        return []

    rowl = len(matrix)
    coll = len(matrix[0])
    first_cell_row_zero = False
    first_cell_col_zero = False

    for row in range(rowl):
        for col in range(coll):
            if matrix[row][col] == 0:
                if row == 0:
                    first_cell_row_zero = True
                if col == 0:
                    first_cell_col_zero = True
                matrix[row][0] = matrix[0][col] = 0

    for row in range(1, rowl):
        for col in range(1, coll):
            matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]

    if first_cell_row_zero:
        for col in range(coll):
            matrix[0][col] = 0

    if first_cell_col_zero:
        for row in range(rowl):
            matrix[row][0] = 0


print(set_zeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
