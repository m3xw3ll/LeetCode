def count_good_substrings(s):
    cnt = 0
    for i in range(len(s) - 2):
        if len((set(s[i:i+3]))) == 3:
            cnt += 1
    return cnt


print(count_good_substrings('xyzzaz'))