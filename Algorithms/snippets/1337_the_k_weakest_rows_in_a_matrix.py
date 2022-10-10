def k_weakest_rows(mat, k):
    soldiers_per_row = [[sum(mat[i]), i] for i in range(len(mat))]
    return [x[1] for x in sorted(soldiers_per_row)][:k]


print(k_weakest_rows(mat=[[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], k=3))
