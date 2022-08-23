def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    if len(nums) % 2 == 0:
        m1 = len(nums) // 2
        m2 = (len(nums) // 2) -1
        return float((nums[m1] + nums[m2]) / 2)
    else:
        return nums[int(len(nums) // 2)]


print(find_median_sorted_arrays([1, 3], [2]))
