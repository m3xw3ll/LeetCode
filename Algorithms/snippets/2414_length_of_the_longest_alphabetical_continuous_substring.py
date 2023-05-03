def longest_continuous_substring(s):
    out = 1
    tmp = 1
    for i in range(len(s) - 1):
        if ord(s[i]) == ord(s[i+1]) - 1:
            tmp += 1
        else:
            tmp = 1
        out = max(out, tmp)
    return out



print(longest_continuous_substring('abcde'))