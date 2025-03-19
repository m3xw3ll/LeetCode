def sum_of_the_digits_of_harshad_number(x):
    s = sum(int(d) for d in str(x))
    return s if x % s == 0 else -1


print(sum_of_the_digits_of_harshad_number(18))