def longest_alternating_subarray(nums, threshold):
    m = 0
    for n in range(len(nums)):
        if nums[n] % 2 == 0 and nums[n] <= threshold:
            m = max(m, 1)
            for r in range(n+1, len(nums)):
                if nums[r-1] % 2 == nums[r] % 2:
                    break
                if nums[r] > threshold:
                    break
                m = max(m, r - n + 1)
    return m


print(longest_alternating_subarray(nums=[2, 4], threshold=7))
