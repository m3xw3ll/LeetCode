def sum_of_three(num):
    if num % 3 != 0:
        return []
    return [num // 3 - 1, num // 3, num // 3 + 1]


print(sum_of_three(33))