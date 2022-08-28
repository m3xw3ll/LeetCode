def restore_string(s, indices):
    out = [[] for i in range(len(s))]
    for i, v in enumerate(indices):
        out[v] = s[i]
    return ''.join(out)


print(restore_string('abc', [0, 1, 2]))
