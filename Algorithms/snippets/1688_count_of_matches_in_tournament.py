def number_of_matches(n):
    m = 0
    while n > 1:
        if n % 2 == 0:
            m += (n / 2)
            n /= 2
        else:
            m += (n // 2)
            n = (n // 2) + 1
    return int(m)


print(number_of_matches(14))