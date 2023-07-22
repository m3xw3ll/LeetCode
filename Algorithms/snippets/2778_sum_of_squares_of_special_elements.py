def sum_of_squares(nums):
    out = 0
    n = len(nums)
    for i in range(1, n + 1):
        if n % i == 0:
            out += nums[i - 1] ** 2
    return out

print(sum_of_squares([1, 2, 3, 4]))