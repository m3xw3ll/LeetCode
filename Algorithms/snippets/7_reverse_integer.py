def reverse(x):
    x = str(x)
    if x[0] == '-':
        x = '-' + x[1:][::-1]
    else:
        x = x[::-1]

    if int(x) not in range(-2**31, 2**31):
        return 0

    return x


print(int(reverse(120)))