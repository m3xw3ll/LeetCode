def difference_of_sums(n, m):
    nums1 = 0
    nums2 = 0
    for i in range(1, n + 1):
        if i % m == 0:
            nums2 += i
        else:
            nums1 += i
    return nums1 - nums2


print(difference_of_sums(n=10, m=3))
