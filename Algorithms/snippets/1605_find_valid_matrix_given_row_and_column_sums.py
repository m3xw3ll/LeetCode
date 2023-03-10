def restore_matrix(row_sum, col_sum):
    r = len(row_sum)
    c = len(col_sum)
    mat = [[0] * c for i in range(r)]
    for r in range(len(row_sum)):
        for c in range(len(col_sum)):
            mat[r][c] = min(row_sum[r], col_sum[c])
            row_sum[r] -= mat[r][c]
            col_sum[c] -= mat[r][c]
    return mat


print(restore_matrix(row_sum=[3, 8], col_sum=[4, 7]))
