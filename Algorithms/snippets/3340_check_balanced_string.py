def is_balanced(num):
    even_sum = 0
    odd_sum = 0
    for i in range(len(num)):
        if i % 2 == 0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])

    return even_sum == odd_sum


print(is_balanced("1234"))