def sort_by_bits(arr):
    bits = []
    out = []
    for i in arr:
        bits.append(str(format(i, '2b')).count('1'))

    tmp = sorted(list(zip(bits, arr)))
    for j in tmp:
        out.append(j[1])
    return out


print(sort_by_bits([0,1,2,3,4,5,6,7,8]))