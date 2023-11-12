def maximum_strong_pair_xor(nums):
    out = -float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                out = max(out, (nums[i] ^ nums[j]))
    return out


print(maximum_strong_pair_xor([1, 2, 3, 4, 5]))