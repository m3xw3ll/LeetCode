def are_similar(mat, k):
    k %= len(mat[0])
    for i in mat:
        if i != i[k:] + i[:k]:
            return False
    return True


print(are_similar(mat = [[2,2],[2,2]], k = 3))
