def max_score(s):
    out = 0
    for i in range(1, len(s)):
        left = s[:i].count('0')
        right = s[i:].count('1')
        out = max(out, left + right)
    return out


print(max_score('00'))