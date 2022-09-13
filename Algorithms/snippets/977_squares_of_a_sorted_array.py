def sorted_squares(nums):
    out = [n ** 2 for n in nums]
    return sorted(out)


print(sorted_squares([-4, -1, 0, 3, 10]))