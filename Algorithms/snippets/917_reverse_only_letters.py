def reverse_only_letters(s):
    s = list(s)
    chars = set('abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ')
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] in chars and s[right] in chars:
            s[left], s[right] = s[right], s[left]
        elif s[left] not in chars:
            left += 1
            continue
        elif s[right] not in chars:
            right -= 1
            continue
        left += 1
        right -= 1
    return ''.join(s)


print(reverse_only_letters('ab-cd'))
