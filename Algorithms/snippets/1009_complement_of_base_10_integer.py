def bitwise_complement(n):
    n = str(format(n, 'b'))
    out = "".join(['1' if x == '0' else '0' for x in n])
    return int(out, 2)


print(bitwise_complement(5))