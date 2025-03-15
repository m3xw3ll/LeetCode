def has_same_digits(s):
    while len(s) != 2:
        new_s = ''
        for i in range(len(s) - 1):
            tmp = (int(s[i]) + int(s[i+1])) % 10
            new_s += str(tmp)
        s = new_s
    return True if s[0] == s[1] else False


print(has_same_digits("3902"))