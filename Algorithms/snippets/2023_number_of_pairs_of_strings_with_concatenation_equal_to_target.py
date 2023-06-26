def num_of_pairs(nums, target):
    cnt = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                cnt += 1
    return cnt


print(num_of_pairs(nums=["777", "7", "77", "77"], target="7777"))
