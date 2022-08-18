def check_string(s):
    if 'a' not in s:
        return True
    i = 0
    while s[i] == 'a':
        i += 1
        if i == len(s):
            break
    while i < len(s):
        if s[i] == 'a':
            return False
        i += 1
    return True


print(check_string('abab'))