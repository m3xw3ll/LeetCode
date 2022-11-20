def fill_cups(amount):
    amount.sort(reverse=True)
    cnt = 0

    while amount[0] > 0:
        amount[0] -= 1
        amount[1] -= 1
        cnt += 1
        amount = sorted(amount, reverse=True)
    return cnt


print(fill_cups([5, 4, 4]))
