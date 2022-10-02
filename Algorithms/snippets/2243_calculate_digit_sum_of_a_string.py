def digit_sum(s, k):
    while len(s) > k:
        sets = [s[x:x+k] for x in range(0, len(s), k)]
        update = ''
        for s in sets:
            update += str((sum(list(map(int, s)))))
        s = update
    return s


print(digit_sum('11111222223', 3))