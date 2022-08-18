def two_out_of_three(nums1, nums2, nums3):
    out = []
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    nums3 = list(set(nums3))

    for i in nums1:
        if i in nums2 or i in nums3:
            out.append(i)
    for i in nums2:
        if i in nums1 or i in nums3:
            out.append(i)
    out = set(out)
    return list(set(out))


print(two_out_of_three([1, 1, 3, 2], [2, 3], [3]))