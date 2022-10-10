def next_greater_element(nums1, nums2):
    out = []
    for num in nums1:
        flag = True
        num2idx = nums2.index(num)
        for i in range(num2idx + 1, len(nums2)):
            if nums2[i] > num:
                out.append(nums2[i])
                flag = False
                break
            else:
                flag = True
                continue
        if flag:
            out.append(-1)
    return out


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))