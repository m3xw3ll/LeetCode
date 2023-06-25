import math


def count_beautiful_pairs(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            d1 = str(nums[i])[0]
            d2 = str(nums[j])[-1]
            if math.gcd(int(d1), int(d2)) == 1:
                cnt += 1
    return cnt


print(count_beautiful_pairs([2, 5, 1, 4]))
