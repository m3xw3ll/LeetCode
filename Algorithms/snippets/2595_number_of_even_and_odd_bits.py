def even_odd_bit(n):
    odds = 0
    evens = 0

    for idx, val in enumerate(bin(n)[2:][::-1]):
        if idx % 2 ==  0 and val == '1':
            evens += 1
        elif idx % 2 == 1 and val == '1':
            odds += 1
    return [evens, odds]


print(even_odd_bit(17))