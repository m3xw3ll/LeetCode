def split_num(num):
    num = ''.join(sorted(str(num)))
    return int(num[::2]) + int(num[1::2])


print(split_num(4325))