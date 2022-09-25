def replace_digits(s):
    out = ''
    for n in range(len(s)):
        if n % 2 == 0:
            out += s[n]
        else:
            out += (chr(ord(s[n-1]) + int(s[n])))
    return out


print(replace_digits('a1b2c3d4e'))