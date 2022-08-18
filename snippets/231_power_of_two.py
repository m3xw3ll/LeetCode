def is_power_of_two(n):
    return n and not (n & n -1)


print(is_power_of_two(4))