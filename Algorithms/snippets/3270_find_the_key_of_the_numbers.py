def generate_key(num1, num2, num3):
    out = ''
    num1 = str(num1).zfill(4)
    num2 = str(num2).zfill(4)
    num3 = str(num3).zfill(4)

    for i in range(4):
        out += min(num1[i], num2[i], num3[i])
    return int(out)


print(generate_key(num1=1, num2=10, num3=1000))
