def convert_to_title(column_number):
    out = ''
    while column_number > 0:
        column_number -= 1
        out = chr(column_number % 26 + 65) + out
        column_number //= 26
    return out


print(convert_to_title(28))