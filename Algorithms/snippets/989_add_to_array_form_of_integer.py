def add_to_array_form(num, k):
    num = int(''.join([str(i) for i in num]))
    return [int(i) for i in str(num+k)]


print(add_to_array_form(num=[1, 2, 0, 0], k=34))
