def count_even(num):
    cnt = 0
    for i in range(2, num+1):
        if sum(int(x) for x in list(str(i))) % 2 == 0:
            cnt += 1
    return cnt


print(count_even(30))