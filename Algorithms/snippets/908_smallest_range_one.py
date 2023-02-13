def smallest_range_one(nums, k):
    if min(nums) + k < max(nums) - k:
        return max(nums) - min(nums) - 2 * k
    return 0


print(smallest_range_one(nums=[1, 3, 6], k=3))
