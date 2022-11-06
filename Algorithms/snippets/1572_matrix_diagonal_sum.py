def diagonal_sum(mat):
    n = len(mat[0])
    out = 0
    for i in range(n):
        out += mat[i][i]
        out += mat[i][n - 1 - i]

    if n % 2 != 0:
        twice = n // 2
        out -= mat[twice][twice]
    return out


print(diagonal_sum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
