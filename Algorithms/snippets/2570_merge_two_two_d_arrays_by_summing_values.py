def merge_arrays(nums1, nums2):
    dic = {}
    for n in nums1:
        dic[n[0]] = n[1]
    for n in nums2:
        if n[0] in dic:
            dic[n[0]] += n[1]
        else:
            dic[n[0]] = n[1]

    return list(sorted(dic.items()))


print(merge_arrays(nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]))
