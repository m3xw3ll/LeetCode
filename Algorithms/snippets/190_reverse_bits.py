def reverse_bits(n):
    n = bin(int(n))
    n = n[2:]
    n = n.zfill(32)
    n = n[::-1]
    return int(n, 2)

print(reverse_bits('11111111111111111111111111111101'))