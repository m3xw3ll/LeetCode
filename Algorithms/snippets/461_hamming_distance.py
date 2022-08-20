def hamming_distance(x, y):
    return str(bin(x^y)).count('1')


print(hamming_distance(3, 1))
