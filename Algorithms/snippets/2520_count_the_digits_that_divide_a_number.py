def count_digits(num):
    cnt = 0
    for val in str(num):
        if num % int(val) == 0:
            cnt += 1
    return cnt

print(count_digits(121))