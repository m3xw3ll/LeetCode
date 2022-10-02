def range_bitwise_and(left, right):
    n = right - left
    x = 0
    for b in range(31, -1, -1):
        if (1 << b) < n:
            break
        if (1 << b) & left & right:
            x += 1 << b
    return x

print(range_bitwise_and(0, 0))