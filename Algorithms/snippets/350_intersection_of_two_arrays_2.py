from collections import Counter

def intersect(nums1, nums2):
    nums1 = Counter(nums1)
    nums2 = Counter(nums2)
    out = []
    for n, c in nums1.items():
        if n in nums2:
            out.extend([n] * min(c, nums2[n]))
    return out


print(intersect([1, 2, 2, 1], [2, 3]))