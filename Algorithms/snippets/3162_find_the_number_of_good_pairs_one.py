def number_of_pairs(nums1, nums2, k):
    cnt = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                cnt += 1
    return cnt


print(number_of_pairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
