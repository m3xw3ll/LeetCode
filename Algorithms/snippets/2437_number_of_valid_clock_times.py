def count_time(time):
    h1, h2, _, m1, m2 = time
    out = 1
    if h1 == '?' and h2 == '?':
        out *= 24
    elif h1 == '?':
        if int(h2) >= 4:
            out *= 2
        else:
            out *= 3
    elif h2 == '?':
        if int(h1) <= 1:
            out *= 10
        else:
            out *= 4

    if m1 == '?' and m2 == '?':
        out *= 60
    elif m1 == '?':
        out *= 6
    elif m2 == '?':
        out *= 10

    return out


print(count_time('?5:00'))