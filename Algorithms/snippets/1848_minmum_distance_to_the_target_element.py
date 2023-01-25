def get_min_distance(nums, target, start):
    out = float('inf')
    for idx, num in enumerate(nums):
        if num == target:
            out = min(out, abs(idx - start))
    return out


print(get_min_distance(nums=[1, 2, 3, 4, 5], target=5, start=3))
