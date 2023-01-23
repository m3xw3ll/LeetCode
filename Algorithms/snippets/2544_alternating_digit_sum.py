def alternating_digit_sum(n):
    out = 0
    n = str(n)
    for i in range(0, len(n), 2):
        out += int(n[i])
    for j in range(1, len(n), 2):
        out -= int(n[j])
    return out


print(alternating_digit_sum(521))