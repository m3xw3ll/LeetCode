def binary_gap(n):
    n = bin(n)[2:]
    found = False
    out = 0
    for i in range(len(n)):
        if n[i] == '1' and not found:
            found = True
            start = i
        elif n[i] == '1' and found:
            dst = i - start
            out = max(out, dst)
            start = i
    return out


print(binary_gap(22))