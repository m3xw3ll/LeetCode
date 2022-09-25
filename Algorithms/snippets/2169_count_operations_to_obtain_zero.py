def count_operations(num1, num2):
    cnt = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        cnt += 1
    return cnt


print(count_operations(2, 3))