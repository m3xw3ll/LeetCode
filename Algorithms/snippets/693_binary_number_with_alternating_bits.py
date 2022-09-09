def has_alternating_bits(n):
    bit = format(n, 'b')
    first = bit[0]
    for b in range(1, len(bit)):
        if bit[b] == first:
            return False
        else:
            first = bit[b]
    return True



print(has_alternating_bits(5))