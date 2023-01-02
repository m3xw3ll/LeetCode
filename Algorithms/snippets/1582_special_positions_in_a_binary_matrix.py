def num_special(mat):
    cnt = 0
    rows = len(mat)
    cols = len(mat[0])
    row_sum = list()
    col_sum = list()

    for r in mat:
        row_sum.append(sum(r))
    for c in zip(*mat):
        col_sum.append(sum(c))

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1 and row_sum[r] == 1 and col_sum[c] == 1:
                cnt += 1
    return cnt


print(num_special(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
