def rotated_digits(n):
    cnt = 0
    for i in range(1, n+1):
        s = set(list(str(i)))
        if (not s.intersection({'3', '4', '7'})) and s.intersection({'2', '5', '6', '9'}):
            cnt += 1
    return cnt


print(rotated_digits(10))