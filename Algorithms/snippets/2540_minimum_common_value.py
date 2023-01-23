def get_common(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    t = list(nums1 & nums2)
    return -1 if len(t) == 0 else min(t)


print(get_common(nums1=[1, 3], nums2=[2, 4]))
