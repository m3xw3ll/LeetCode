def matrix_reshape(mat, r, c):
    flat = []
    out = []

    for row in mat:
        for num in row:
            flat.append(num)

    if len(flat) != r * c:
        return mat
    else:
        for i in range(r):
            out.append(flat[i*c:i*c+c])
    return out


print(matrix_reshape(mat=[[1, 2], [3, 4]], r=1, c=4))
