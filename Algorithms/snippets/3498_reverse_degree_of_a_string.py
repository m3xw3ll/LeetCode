def reverse_degree(s):
    out = 0
    idx = 1
    for char in s:
        out += (ord('z') - ord(char) + 1) * idx
        idx += 1
    return out


print(reverse_degree('abc'))