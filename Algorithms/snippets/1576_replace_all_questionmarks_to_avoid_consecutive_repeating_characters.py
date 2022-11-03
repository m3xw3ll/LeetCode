def modify_string(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            for char in 'abc':
                if (i == 0 or s[i-1] != char) and (i+1 == len(s) or s[i+1] !=char):
                    s[i] = char
                    break
    return ''.join(s)


print(modify_string('?zs'))