def count_quadruplets(nums):
    cnt = 0
    l = len(nums)
    for a in range(l):
        for b in range(a + 1, l):
            for c in range(b + 1, l):
                for d in range(c + 1, l):
                    if a < b < c < d and nums[a] + nums[b] + nums[c] == nums[d]:
                        cnt += 1
    return cnt


print(count_quadruplets([1, 2, 3, 6]))
