def distinct_averages(nums):
    avgs = set()
    nums.sort()
    i, j = 0, len(nums) - 1

    while i < j:
        avgs.add((nums[i] + nums[j]) / 2)
        i += 1
        j -= 1
    return len(avgs)


print(distinct_averages([4, 1, 4, 0, 3, 5]))
