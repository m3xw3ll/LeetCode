def find_the_array_conc_val(nums):
    out = 0
    for i in range(len(nums) // 2):
        out += int((str(nums[i]) + str(nums[len(nums) - 1 - i])))

    if len(nums) % 2 != 0:
        out += nums[len(nums) // 2]
    return out


print(find_the_array_conc_val([5, 14, 13, 8, 12]))
