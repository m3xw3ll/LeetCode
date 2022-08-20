def str_str(haystack, needle):
    left = 0
    right = len(needle)
    while right <= len(haystack):
        if haystack[left:right] == needle:
            return left
        left += 1
        right += 1
    return -1


print(str_str('hello', 'll'))