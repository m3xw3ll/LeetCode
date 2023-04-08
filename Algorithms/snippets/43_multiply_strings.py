def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'

    digits = {'1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9}

    v1 = 0
    v2 = 0

    for i in num1:
        v1 = 10 * v1 + digits[i]
    for j in num2:
        v2 = 10 * v2 + digits[j]

    return str(v1 * v2)


print(multiply(num1="2", num2="3"))
