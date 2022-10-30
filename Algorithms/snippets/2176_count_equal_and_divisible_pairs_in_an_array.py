def count_pairs(nums, k):
    l = len(nums)
    cnt = 0
    for i in range(0, l):
        for j in range(i + 1, l):
            if nums[i] == nums[j] and (i * j) % k == 0:
                cnt += 1
    return cnt


print(count_pairs([3, 1, 2, 2, 2, 1, 3], 2))
