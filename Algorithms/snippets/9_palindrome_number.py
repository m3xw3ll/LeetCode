def is_palindrome(x):
    n = str(x)
    m = n[::-1]
    if n == m:
        return True
    else:
        return False


print(is_palindrome(-121))
