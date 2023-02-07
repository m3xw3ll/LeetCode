def separate_digits(nums):
    return [int(x) for n in nums for x in str(n)]


print(separate_digits([13, 25, 83, 77]))
