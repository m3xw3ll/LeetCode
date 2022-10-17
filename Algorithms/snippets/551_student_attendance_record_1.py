def check_record(s):
    for i in range(0, len(s) - 2):
        sub = s[i:i+3]
        if sub.count('L') == 3:
            return False
    if s.count('A') >= 2:
        return False
    return True


print(check_record('PPALLL'))