def maximum_odd_binary_number(s):
    if s.count('1') == 1:
        return ''.join(sorted(s))
    return '1' * (s.count('1') - 1) + '0' * s.count('0') + '1'


print(maximum_odd_binary_number('0101'))