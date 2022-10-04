from collections import Counter

def find_kth_largest(nums, k):
    mini = min(nums)
    maxi = max(nums)
    c = Counter(nums)
    curr = 0

    for i in range(maxi, mini -1, -1):
        curr += c[i]
        if curr >= k:
            return i
    return -1

print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))
