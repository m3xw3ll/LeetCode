def max_power(s):
    c = 1
    out = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            c += 1
            out = max(c, out)
        else:
            c = 1
    return out


print(max_power('leetcode'))
