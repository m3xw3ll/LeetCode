def min_bit_flips(start, goal):
    return bin(start ^ goal).count('1')


print(min_bit_flips(10, 7))
