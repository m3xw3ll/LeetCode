def count_elements(nums):
    mini = min(nums)
    maxi = max(nums)
    return sum(1 for n in nums if mini < n < maxi)


print(count_elements([-3, 3, 3, 90]))
