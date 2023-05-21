def process_queries(queries, m):
    p = [i for i in range(1, m + 1)]
    out = []
    for q in queries:
        idx = p.index(q)
        out.append(idx)
        p.remove(q)
        p.insert(0, q)
    return out


print(process_queries(queries=[3, 1, 2, 1], m=5))
