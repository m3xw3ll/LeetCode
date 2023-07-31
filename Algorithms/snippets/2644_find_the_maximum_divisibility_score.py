def max_div_score(nums, divisors):
    out = -1
    most_cnt = -1

    for d in divisors:
        cnt = sum(1 for n in nums if n % d == 0)
        if cnt > most_cnt or (cnt == most_cnt and d < out):
            out = d
            most_cnt = cnt
    return out


print(max_div_score(nums=[4, 7, 9, 3, 9], divisors=[5, 2, 3]))
