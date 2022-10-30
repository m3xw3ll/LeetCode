def average_value(nums):
    l = 0
    s = 0
    for n in nums:
        if n % 6 == 0:
            s += n
            l += 1
    return s // l


print(average_value([1, 3, 6, 10, 12, 16]))
