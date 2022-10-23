def find_content_children(g, s):
    i = j = out = 0
    g.sort()
    s.sort()

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            out += 1
            i += 1
        j += 1
    return out


print(find_content_children([1, 2, 3], [1, 1]))