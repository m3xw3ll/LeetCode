def maximum_triplet_value(nums):
    trip_value = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                trip_value = max(trip_value, ((nums[i] - nums[j]) * nums[k]))
    return trip_value


print(maximum_triplet_value([12, 6, 1, 2, 7]))
