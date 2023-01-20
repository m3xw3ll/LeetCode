def add_spaces(s, spaces):
    out = list()
    i = len(s) -1
    while i >= 0:
        out.append(s[i])
        if spaces and i == spaces[-1]:
            out.append(' ')
            spaces.pop()
        i -= 1
    return ''.join(out)[::-1]


print(add_spaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
