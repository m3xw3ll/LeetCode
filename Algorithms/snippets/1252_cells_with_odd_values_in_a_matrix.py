def odd_cells(m, n, indices):
    rows = [0] * m
    cols = [0] * n

    for row, col in indices:
        rows[row] ^= 1
        cols[col] ^= 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if rows[i] ^ cols[j] == 1:
                cnt += 1
    return cnt


print(odd_cells(m=2, n=3, indices=[[0, 1], [1, 1]]))
