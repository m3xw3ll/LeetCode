def sum_base(n, k):
    out = ''
    while n > 0:
        rm = n % k
        out = str(rm) + out
        n = n // k
    return sum(int(i) for i in out)


print(sum_base(34, 6))
