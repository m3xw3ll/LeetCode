def licence_key_formatting(s, k):
    s = s.upper()[::-1]
    s = s.replace('-', '')
    out = [s[i:i+k] for i in range(0, len(s), k)]
    return '-'.join(out)[::-1]


print(licence_key_formatting('2-5g-3-J', 2))
