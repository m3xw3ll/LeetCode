def reformat(s):
    chrs = [x for x in s if x.isalpha()]
    digs = [x for x in s if x.isdigit()]

    if abs(len(chrs) - len(digs)) >= 2: return ''
    out = []
    flag = len(chrs) > len(digs)

    while chrs or digs:
        out.append(chrs.pop() if flag else digs.pop())
        flag = not flag
    return ''.join(out)

print(reformat('a0b1c2'))