def smaller_numbers_than_current(nums):
    out = []
    for i in range(len(nums)):
        max = nums[i]
        cnt = 0
        for j in range(len(nums)):
            if nums[j] < max:
                cnt += 1
        out.append(cnt)
    return out


print(smaller_numbers_than_current([8, 1, 2, 2, 3]))