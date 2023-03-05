def combine(n, k):
    out = []

    def backtrack(i, cur):
        if len(cur) == k:
            out.append(cur.copy())
            return
        for j in range(i, n):
            cur.append(j+1)
            backtrack(i + 1, cur)
            cur.pop()
            i += 1

    backtrack(0, [])
    return out


print(combine(n=4, k=2))