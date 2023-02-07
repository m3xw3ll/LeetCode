def check_perfect_number(num):
    if num == 1:
        return False

    sqr = int(num ** 0.5)
    s = 1
    for i in range(2, sqr + 1):
        if num % i == 0:
            t = num // i
            s += t + i
    return True if s == num else False


print(check_perfect_number(28))