def divisor_substrings(num, k):
    s = str(num)
    out = 0
    for i in range(k, len(s)+1):
        x = int((s[i-k:i]))
        if x != 0 and num % x == 0:
            out += 1
    return out


print(divisor_substrings(240, 2))