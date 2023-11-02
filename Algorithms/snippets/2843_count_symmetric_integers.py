def count_symmetric_integers(low, high):
    cnt = 0
    nums = [num for num in range(low, high + 1) if len(str(num)) % 2 == 0]
    for n in nums:
        m = len(str(n)) // 2
        first = [int(x) for x in list(str(n)[:m])]
        second = [int(x) for x in list(str(n)[m:])]
        if sum(first) == sum(second):
            cnt += 1
    return cnt


print(count_symmetric_integers(low=1200, high=1230))
