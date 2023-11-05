def min_operations(n):
    if n % 2 != 0:
        return (n + 1) * (n // 2) / 2
    else:
        return n * (n // 2) / 2


print(min_operations(6))