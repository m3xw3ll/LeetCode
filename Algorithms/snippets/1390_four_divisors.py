def sum_four_divisors(nums):
    s = 0
    for n in nums:
        tmp = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                tmp.add(i)
                tmp.add(n // i)
            if len(tmp) > 4:
                break
        if len(tmp) == 4:
            s += sum(tmp)
    return s


print(sum_four_divisors([21, 4, 7]))
