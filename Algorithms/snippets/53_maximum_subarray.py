def max_sub_array(nums):
    best_sum = float('-inf')
    cur_sum = 0
    for n in nums:
        cur_sum = max(n, cur_sum + n)
        best_sum = max(best_sum, cur_sum)
    return best_sum


print(max_sub_array([-1]))
