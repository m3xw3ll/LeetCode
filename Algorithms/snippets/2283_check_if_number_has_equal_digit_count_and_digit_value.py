def digit_count(num):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) == num.count(str(i)):
            pass
        else:
            return False
    return True


print(digit_count(1210))
