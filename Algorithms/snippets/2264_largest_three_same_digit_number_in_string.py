def largest_good_integer(num):
    cnt = 1
    out = ''
    for i in range(1, len(num)):
        if num[i-1] == num[i]:
            cnt += 1
        else:
            cnt = 1
        if cnt == 3:
            out = max(out, num[i] * 3)
    return out


print(largest_good_integer("3200014888"))
