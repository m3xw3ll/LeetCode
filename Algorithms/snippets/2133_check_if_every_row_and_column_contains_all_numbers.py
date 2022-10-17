def check_valid(matrix):
    n = len(matrix)
    for row, column in zip(matrix, zip(*matrix)):
        if len(set(row)) != n or len(set(column)) != n:
            return False
    return True


print(check_valid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
