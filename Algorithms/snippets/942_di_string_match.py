def di_string_match(s):
    low = 0
    high = len(s)
    out = []

    for x in s:
        if x == 'I':
            out.append(low)
            low += 1
        else:
            out.append(high)
            high -= 1

    return out + [low]


print(di_string_match('IDDI'))