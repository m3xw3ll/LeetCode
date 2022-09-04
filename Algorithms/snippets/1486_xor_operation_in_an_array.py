def xor_operation(n, start):
    out = 0
    nums = [i for i in range(start, start + 2 * (n), 2)]
    for n in nums:
        out ^= n
    return out


print(xor_operation(5, 0))