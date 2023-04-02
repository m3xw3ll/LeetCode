def min_number(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    both = nums1.intersection(nums2)
    if len(both) >= 1:
        return sorted(list(both))[0]

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    n1, n2 = min(nums1), min(nums2)
    return min(n1, n2) * 10 + max(n1, n2)


print(min_number(nums1=[5, 8, 2, 7], nums2=[5, 2, 8, 4, 7, 1, 3]))
