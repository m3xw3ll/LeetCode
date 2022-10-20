def check_zero_ones(s):
    ones = s.split('0')
    zeros = s.split('1')

    max_one = max(ones, key=len)
    max_zero = max(zeros, key=len)

    if max_one > max_zero:
        return True
    return False


print(check_zero_ones('1101'))