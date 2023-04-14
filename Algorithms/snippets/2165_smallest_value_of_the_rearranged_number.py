def smallest_number(num):
    if num == 0:
        return 0

    out = ''
    zero = ''

    for n in str(num):
        if n != '-':
            if n == '0':
                zero += n
            else:
                out += n
    out = ''.join(sorted(out))

    if num < 0:
        return -1 * int(out[::-1] + zero)
    elif out and zero:
        print(out, zero)
        return int(out[0] + zero + out[1:])
    else:
        return int(out)


print(smallest_number(310))