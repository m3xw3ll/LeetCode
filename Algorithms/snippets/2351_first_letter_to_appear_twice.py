def repeated_character(s):
    seen = set()
    for i in range(len(s)):
        if s[i] in seen:
            return s[i]
        else:
            seen.add(s[i])

print(repeated_character('abccbaacz'))