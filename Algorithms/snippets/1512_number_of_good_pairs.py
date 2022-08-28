def num_identical_pairs(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if i < j and nums[i] == nums[j]:
                cnt += 1
    return cnt

print(num_identical_pairs([1, 2, 3, 1, 1, 3]))