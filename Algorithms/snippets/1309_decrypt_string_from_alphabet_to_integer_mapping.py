def freq_alphabet(s):
    out = ''
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i+2] == '#':
            out += chr(int(s[i:i+2]) + 96)
            i += 3
        else:
            out += chr(int(s[i]) + 96)
            i += 1
    return out


print(freq_alphabet('10#11#12'))