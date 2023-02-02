def largest_sum_after_k_negations(nums, k):
    i = 0
    while i < k:
        m = min(nums)
        min_idx = nums.index(m)
        nums[min_idx] = m * -1
        i += 1
    return sum(nums)


print(largest_sum_after_k_negations(nums=[4, 2, 3], k=1))
