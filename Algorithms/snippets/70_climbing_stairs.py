def climbing_stairs(n):
    fib = [1, 2, 3]
    if n < 4:
        return n
    else:
        for i in range(3, n):
            fib.append(fib[i-1] + fib[i-2])
    return fib[-1]


print(climbing_stairs(4))