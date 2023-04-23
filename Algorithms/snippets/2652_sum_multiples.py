def sum_of_multiples(n):
    cnt = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            cnt += i
    return cnt


print(sum_of_multiples(7))