def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    return list(nums1 & nums2)


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))