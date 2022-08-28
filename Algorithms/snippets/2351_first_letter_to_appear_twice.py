def repeated_character(s):
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            return prev
        prev = s[i]

print(repeated_character('abccbaacz'))