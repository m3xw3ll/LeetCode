def minimum_sum(num):
    num = sorted([int(n) for n in str(num)])
    num1 = int(str(num[0]) + str(num[2]))
    num2 = int(str(num[1]) + str(num[3]))
    return num1 + num2


print(minimum_sum(2932))