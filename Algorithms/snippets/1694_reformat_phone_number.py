def reformat_number(number):
    number = ''.join(number.split())
    number = number.replace('-', '')
    out = []
    for i in range(0, len(number), 3):
        if len(number) - i != 4:
            out.append(number[i:i+3])
        else:
            out.extend([number[i:i+2], number[i+2:]])
            break
    return '-'.join(out)


print(reformat_number('1-23-45- 6'))