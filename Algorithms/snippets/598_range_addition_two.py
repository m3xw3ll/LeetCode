def max_count(m, n, ops):
    for x, y in ops:
        print(x, y)
        m = min(m, x)
        n = min(n, x)
    return m * n


print(max_count(m=3, n=3, ops=[[2, 2], [3, 3]]))
