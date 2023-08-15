def count_complete_subarrays(nums):
    cnt = 0
    dist_elements = len(set(nums))
    for i in range(len(nums)):
        tmp = set()
        for j in range(i, len(nums)):
            tmp.add(nums[j])
            if len(tmp) == dist_elements:
                cnt += 1
    return cnt


print(count_complete_subarrays([1, 3, 1, 2, 2]))
