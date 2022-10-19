def minimum_moves(s):
    cnt = 0
    i = 0
    while i < len(s):
        if s.count('X') == 0:
            break
        elif s[i] == 'X':
            cnt += 1
            i += 2
        i += 1
    return cnt


print(minimum_moves('XXOX'))