def sum_zero(n):
    out = list()
    if n % 2 != 0:
        out.append(0)
    for i in range(1, n, 2):
        out.append(i)
        out.append(-i)
    return out


print(sum_zero(3))