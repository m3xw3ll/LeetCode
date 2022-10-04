def transpose(matrix):
    out = []
    for c in range(len(matrix[0])):
        out.append([0] * len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            out[j][i] = matrix[i][j]
    return out


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
