def cells_in_range(s):
    out = list()
    c1, c2, c3, c4 = s[0], s[1], s[3], s[4]
    for i in range(ord(c1), ord(c3)+1):
        for j in range(int(c2), int(c4)+1):
            out.append(chr(i) + str(j))
    return out


print(cells_in_range('K1:L2'))