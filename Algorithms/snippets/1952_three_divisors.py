def is_three(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
        if cnt > 3:
            return False

    return True if cnt == 3 else False


print(is_three(4))
