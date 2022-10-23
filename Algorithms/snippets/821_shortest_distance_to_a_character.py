def shortest_to_char(s, c):
    target_idxs = []
    for idx, val in enumerate(s):
        if val == c:
            target_idxs.append(idx)
    out = []
    for i in range(len(s)):
        out.append(min([abs(t-i) for t in target_idxs]))
    return out


print(shortest_to_char('loveleetcode', 'e'))