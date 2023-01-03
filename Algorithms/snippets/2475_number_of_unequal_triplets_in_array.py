def unequal_triplets(nums):
    out = 0
    for i in range(len(nums) - 2):
        for j in range(i, len(nums) - 1):
            for k in range(j, len(nums)):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    out += 1
    return out


print(unequal_triplets([4, 4, 2, 4, 3]))
