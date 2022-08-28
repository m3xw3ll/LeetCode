def thousand_separator(n):
    if len(str(n)) <= 3:
        return str(n)
    n = str(n)[::-1]
    out = []
    for i in range(0, len(n), 3):
        out.append(n[i:i+3])
    return '.'.join(out)[::-1]


print(thousand_separator(1234))
