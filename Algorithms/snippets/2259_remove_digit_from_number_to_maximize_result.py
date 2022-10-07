def remove_digit(number, digit):
    out = []
    for i in range(len(number)):
        if number[i] == digit:
            out.append(number[:i] + number[i+1:])
    return max(out)


print(remove_digit('123', '3'))
