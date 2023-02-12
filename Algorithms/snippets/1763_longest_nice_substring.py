def longest_nice_substring(s):
    if len(s) < 2: return ""
    chars = set(list(s))

    for i in range(len(s)):
        if s[i].swapcase() not in chars:
            s1 = longest_nice_substring(s[:i])
            s2 = longest_nice_substring(s[i+1:])
            return s2 if len(s2) > len(s1) else s1
    return s


print(longest_nice_substring("YazaAay"))