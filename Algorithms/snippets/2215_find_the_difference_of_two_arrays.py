def find_difference(nums1, nums2):
    out = []
    first = set(nums1) - set(nums2)
    second = set(nums2) - set(nums1)
    out.append(list(first))
    out.append(list(second))
    return out


print(find_difference([1, 2, 3], [2, 4, 6]))