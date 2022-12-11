def pivot_integer(n):
    s = sum([i for i in range(1, n+1)])
    cum = 0
    for i in range(1, n+1):
        cum += i
        if cum  == s - cum + i:
            return i
    return -1


print(pivot_integer(8))