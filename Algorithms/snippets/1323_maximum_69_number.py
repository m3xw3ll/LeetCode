def maximum_number(num):
    s = list(str(num))
    for n in range(len(s)):
        if s[n] == '6':
            s[n] = '9'
            break
    return ''.join(s)


print(maximum_number(9669))