def find_the_difference(s, t):
    sum_s = [sum(ord(i) for i in s)]
    sum_t = [sum(ord(j) for j in t)]
    return chr(abs(sum_s[0] - sum_t[0]))


print(find_the_difference('abcd', 'abcde'))
