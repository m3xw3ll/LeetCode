def judge_square_sum(c):
    root = int(c ** 0.5)
    left = 0
    right = root

    while left <= right:
        res = left ** 2 + right ** 2

        if res == c:
            return True
        elif res > c:
            right -= 1
        else:
            left += 1

    return False


print(judge_square_sum(5))