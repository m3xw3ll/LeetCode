def number_of_cuts(n):
    if n == 1:
        return 0
    return n if n % 2 != 0 else n // 2


print(number_of_cuts(3))
