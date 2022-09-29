def lexical_order(n):
    out = []
    for i in range(1, n+1):
        out.append(i)
    return sorted(out, key=str)


print(lexical_order(13))