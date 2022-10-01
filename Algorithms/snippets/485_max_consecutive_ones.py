def find_max_consecutive_ones(nums):
    cnt = 0
    max_cnt = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 0
    return max(cnt, max_cnt)


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
