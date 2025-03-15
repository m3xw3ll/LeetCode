def has_trailing_zeros(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            xor = nums[i] | nums[j]
            if bin(xor)[2:][-1] == '0':
                return True
    return False


print(has_trailing_zeros([1, 3, 5, 7, 9]))
