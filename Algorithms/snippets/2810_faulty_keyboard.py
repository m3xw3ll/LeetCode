def final_string(s):
    if 'i' not in s: return s
    out = ''
    for char in s:
        if char == 'i':
            out = out[::-1]
        else:
            out += char
    return out


print(final_string('poiinter'))