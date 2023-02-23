def special(nums):
    cnt = 0
    for i in range(1, 1001):
        cnt = 0
        for j in nums:
            if i <= j:
                cnt += 1
        if i == cnt:
            return i
    return -1

print(special([3, 5]))
