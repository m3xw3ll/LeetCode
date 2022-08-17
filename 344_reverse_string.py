def reverse_string(s):
    right_idx = 1
    left_idx = 1
    l = len(s)

    while right_idx + left_idx <= l:
        s[left_idx-1], s[l-right_idx] = s[l-right_idx], s[left_idx-1]
        right_idx += 1
        left_idx += 1
    print(s)


reverse_string(["h","e","l","l","o"])