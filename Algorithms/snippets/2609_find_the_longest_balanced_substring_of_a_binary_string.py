def find_longest_balanced_substring(s):
    tmp = '01'
    out = 0
    while len(tmp) <= len(s):
        if tmp in s:
            out = len(tmp)
        tmp = '0' + tmp + '1'
    return out


print(find_longest_balanced_substring('01000111'))