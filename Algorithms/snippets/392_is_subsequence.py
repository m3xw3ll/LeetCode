def is_subsequence(s, t):
    s_pointer = t_pointer = 0
    while len(s) > s_pointer and len(t) > t_pointer:
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
            t_pointer += 1
        else:
            t_pointer += 1
    if s_pointer == len(s):
        return True
    return False


print(is_subsequence('abc', 'ahbgdc'))