def divide_string(s, k, fill):
    out = []
    i = 0
    l = (len(s))
    while i < l:
        out.append(s[i:i+k])
        i += k
    rem = out[-1]
    if len(rem) < k:
        out[-1] = rem.ljust(k, fill)
    return out


print(divide_string(s='ctoyjrwtngqwt', k=80, fill='n'))
