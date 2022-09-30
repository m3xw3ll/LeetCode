def greatest_letter(s):
    s = set(s)
    upper = ord('Z')
    lower = ord('z')
    for i in range(26):
        if chr(upper - i) in s and chr(lower - i) in s:
            return chr(upper - i)
    return ''


print(greatest_letter('lEeTcOdE'))
