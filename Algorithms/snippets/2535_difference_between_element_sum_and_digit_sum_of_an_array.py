def difference_of_sum(nums):
    element_sum = sum(nums)
    digit_sum = 0
    for n in nums:
        n = str(n)
        for dig in n:
            digit_sum += int(dig)
    return abs(element_sum - digit_sum)


print(difference_of_sum([1, 15, 6, 3]))