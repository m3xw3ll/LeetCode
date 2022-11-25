def longest_palindrome(s):
    dic = {}
    odd = 0
    out = 0
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1

    for f in dic.values():
        out += f
        if f % 2 != 0:
            odd += 1
    if odd == 0:
        return out - odd
    else:
        return out - odd + 1


print(longest_palindrome('abccccdd'))