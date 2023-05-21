def min_length(s):
    while 'AB' in s or 'CD' in s:
        if 'AB' in s:
            s = s.replace('AB', '')
        elif 'CD' in s:
            s = s.replace('CD', '')
    return len(s)


print(min_length('ABFCACDB'))