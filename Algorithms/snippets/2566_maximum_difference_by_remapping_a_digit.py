def min_max_difference(num):
    num = str(num)
    i = 0
    while num[i] == '9' and i < len(num) - 1:
        i += 1
    return int(num.replace(num[i], '9')) - int(num.replace(num[0], '0'))


print(min_max_difference(90))