def trailing_zeroes(n):
    cnt = 0
    i = 5

    while (n / i >= 1):
        cnt += int(n/i)
        i *= 5
    return int(cnt)


print(trailing_zeroes(4))