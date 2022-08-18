def dominant_index(nums):
    largest = max(nums)
    idx = nums.index(largest)
    nums = sorted(nums)

    if nums[-2] * 2 <= nums[-1]:
        return idx
    return -1


print(dominant_index([1, 2, 3, 4]))