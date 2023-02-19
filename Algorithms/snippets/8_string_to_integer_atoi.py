def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = -1 if s[0] == '-' else 1
    s = s[1:] if s[0] in ['-', '+'] else s
    out = 0
    for char in s:
        if not char.isdigit():
            break
        out = out * 10 + int(char)

    if out * sign >= 2**31 - 1:
        return 2 ** 31 - 1
    elif out * sign <= -2**31:
        return -2**31
    else:
        return sign * out

print(my_atoi('   -42'))