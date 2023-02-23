def repeated_substring_pattern(s):
    l = len(s)
    for i in range(0, l // 2):
        ss = s[0:i+1]
        if ss * (len(s) // len(ss)) == s:
            return True
    return False


print(repeated_substring_pattern('abab'))