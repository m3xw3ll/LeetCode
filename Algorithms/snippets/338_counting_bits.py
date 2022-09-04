def count_bits(n):
    out = []
    for i in range(n+1):
        out.append((str(format(i, 'b')).count('1')))
    return out


print(count_bits(2))