def remove_palindrome_sub(s):
    if (len(s)) == 0:
        return 0
    elif s == s[::-1]:
        return 1
    else:
        return 2


print(remove_palindrome_sub('abb'))