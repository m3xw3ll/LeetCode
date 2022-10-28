def get_no_zero_integers(n):
    for i in range(1, n):
        if '0' in str(i) or '0' in str(n-i):
            continue
        return [i, n-i]


print(get_no_zero_integers(11))