def partitions_string(s):
    tmp = set()
    cnt = 1
    for c in s:
        if c in tmp:
            cnt += 1
            tmp = set()
        tmp.add(c)
    return cnt


print(partitions_string('abacaba'))