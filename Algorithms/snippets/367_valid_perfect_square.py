def is_perfect_square(num):
    left = 1
    right = num

    while left <= right:
        middle = (left + right) // 2
        if middle * middle > num:
            right = middle - 1
        elif middle * middle < num:
            left = middle + 1
        else:
            return True
    return False


print(is_perfect_square(16))