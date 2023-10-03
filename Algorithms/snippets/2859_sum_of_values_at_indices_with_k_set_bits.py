def sum_indices_with_k_set_bits(nums, k):
    out = 0
    for idx, val in enumerate(nums):
        if str(bin(idx)[2:]).count('1') == k:
            out += val
    return out


print(sum_indices_with_k_set_bits(nums=[5, 10, 1, 5, 2], k=1))
