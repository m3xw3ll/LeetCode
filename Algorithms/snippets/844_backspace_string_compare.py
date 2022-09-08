def backspace_compare(s, t):
    ss = []
    tt = []

    for i in range(len(s)):
        if s[i] != '#':
            ss.append(s[i])
        if s[i] == '#' and len(ss) > 0:
            ss.pop()

    for j in range(len(t)):
        if t[j] != '#':
            tt.append(t[j])
        if t[j] == '#' and len(tt) > 0:
            tt.pop()

    return True if ss == tt else False


print(backspace_compare('y#fo##f', 'y#f#o##f'))