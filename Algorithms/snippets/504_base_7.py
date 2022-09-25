def convert_to_base_seven(num):
    out = ''
    sign = False

    if num < 0:
        sign = True
        num = abs(num)

    if num == 0:
        return "0"
    while num > 0:
        rm = num % 7
        out = str(rm) + out
        num = num // 7

    if sign:
        out = '-' + out

    return out


print(convert_to_base_seven(100))