def add_digits(num):
    while num >= 10:
        num = sum(int(i) for i in str(num))
    return num


print(add_digits(1))