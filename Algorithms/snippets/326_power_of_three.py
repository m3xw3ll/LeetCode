def is_power_of_three(n):
    x = 1
    while x <= n:
        if x != n:
            x *= 3
        else:
            return True
    return False


print(is_power_of_three(27))