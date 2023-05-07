def check_possibility(nums):
    tmp = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if tmp == 1:
                return False
            tmp += 1
            if i >= 2 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
    return True


print(check_possibility([3, 4, 2, 3]))
