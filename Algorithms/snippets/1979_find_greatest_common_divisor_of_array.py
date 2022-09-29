def find_gcd(nums):
    nums = sorted(nums)
    low = nums[0]
    high = nums[-1]

    while 1:
        r = low % high
        if not r:
            break
        low = high
        high = r
    return high


print(find_gcd([2, 5, 6, 9, 10]))
