def min_operations(s):
    out = [0] * 2
    for i, c in enumerate(s):
        out[i % 2 == int(c)] += 1
    return min(out)


print(min_operations('0100'))