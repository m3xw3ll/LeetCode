def construct_2d_array(original, m, n):
    out = []
    if m * n == len(original):
        for i in range(m):
            out.append(original[i*n:(i+1)*n])
        return out


print(construct_2d_array([1, 2, 3], 1, 3))
