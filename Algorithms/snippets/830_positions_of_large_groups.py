def large_group_positions(s):
    out = list()
    i = 0
    j = 0
    l = len(s)

    while i < l:
        while j < l and s[i] == s[j]:
            j += 1
        if j - i >= 3:
            out.append([i, j - 1])
        i = j
    return out


print(large_group_positions('abbxxxxzzy'))