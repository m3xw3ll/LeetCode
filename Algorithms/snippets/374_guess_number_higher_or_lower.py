def guess(my_guess, pick):
    if my_guess > pick:
        return -1
    elif my_guess < pick:
        return 1
    else:
        return 0


def guess_number(n, pick):
    left = 0
    right = n
    while left < right:
        middle = (left + right) // 2
        if guess(middle, pick) == 0:
            return middle
        elif guess(middle, pick) == -1:
            right = middle -1
        else:
            left = middle +1
    return left


print(guess_number(10, 6))