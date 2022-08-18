def valid_palindrome(s):
    s = ''.join([i for i in s if i.isalnum()]).lower()
    rev = s[::-1]
    for i in range(len(s)):
        if s[i] != rev[i]:
            return False
    return True


print(valid_palindrome("0P"))