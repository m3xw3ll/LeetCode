def is_happy(n):
    stp = {1}
    while n not in stp:
        stp.add(n)
        n = sum([int(i) ** 2 for i in (str(n))])
    return n == 1



print(is_happy(19))