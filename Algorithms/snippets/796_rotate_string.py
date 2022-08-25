def rotate_string(s, goal):
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False


print(rotate_string('abcde', 'abced'))