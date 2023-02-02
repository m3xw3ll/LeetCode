def is_one_bit_character(bits):
    tmp = 0
    i = 0
    while i < len(bits):
        if bits[i] == 0:
            tmp = 0
            i += 1
        else:
            tmp = 1
            i += 2
    return True if tmp == 0 else False


print(is_one_bit_character([1, 1, 0]))