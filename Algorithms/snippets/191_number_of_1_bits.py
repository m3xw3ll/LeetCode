def hamming_weight(n):
    return str(bin(n)).count('1')


print(hamming_weight(0o00000000000000000000000000001011))
