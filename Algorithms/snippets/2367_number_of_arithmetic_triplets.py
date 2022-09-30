def arithmetic_triplets(nums, diff):
    nums = set(nums)
    cnt = 0
    for num in nums:
        if num + diff in nums and num + (2 * diff) in nums:
            cnt += 1
    return cnt


print(arithmetic_triplets([0, 1, 4, 6, 7, 10], 3))
