def balanced_strings(s):
    out = 0
    cnt = 0

    for i in s:
        if i == 'L':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            out += 1
    return out


print(balanced_strings('RLRRLLRLRL'))