def row_and_maximum_ones(mat):
    out = [0, 0]
    for idx, row in enumerate(mat):
        if row.count(1) > out[1]:
            out = [idx, row.count(1)]
    return out


print(row_and_maximum_ones(mat=[[0, 0, 0], [0, 1, 1]]))
