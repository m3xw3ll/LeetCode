def can_alice_win(nums):
    sum_ones = sum(x for x in nums if x <= 9)
    sum_twos = sum(nums) - sum_ones
    return True if (sum_ones > sum_twos or sum_twos > sum_ones) else False


print(can_alice_win([9, 9, 18]))
