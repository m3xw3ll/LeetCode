def make_smallest_palindrome(s):
    left = 0
    right = len(s) - 1
    out = [0] * len(s)
    while left < len(s) / 2:
        out[left] = min(s[left], s[right])
        out[right] = out[left]
        left += 1
        right -= 1
    return ''.join(out)


print(make_smallest_palindrome('egcfe'))