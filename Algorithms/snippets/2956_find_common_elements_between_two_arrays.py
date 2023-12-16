def find_intersection_values(nums1, nums2):
    t = set(nums1)& set(nums2)
    n1 = sum(nums1.count(value) for value in t)
    n2 = sum(nums2.count(value) for value in t)
    return [n1, n2]


print(find_intersection_values(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
