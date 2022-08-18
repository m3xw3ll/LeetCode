def plus_one(digits):
    str_digits = [str(d) for d in digits]
    str_of_digits = "".join(str_digits)
    num = int(str_of_digits) + 1
    return list(str(num))


print(plus_one([1, 2, 3]))