def four_sum(nums, target):
    if len(nums) < 4:
        return []
    tmp = []
    out = []
    nums.sort()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    tmp.append((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
    for i in list(set(tmp)):
        out.append(list(i))
    return out


print(four_sum(nums=[1, 0, -1, 0, -2, 2], target=0))
