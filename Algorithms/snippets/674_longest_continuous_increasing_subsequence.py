def find_length_of_lcis(nums):
    cnt = 1
    tmp = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            tmp += 1
        else:
            cnt = max(cnt, tmp)
            tmp = 1
    return max(cnt, tmp)


print(find_length_of_lcis([1, 3, 5, 7]))
