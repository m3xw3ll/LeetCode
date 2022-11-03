def is_toeplitz_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] != matrix[r-1][c-1]:
                return False
    return True


print(is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
