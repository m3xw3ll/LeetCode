def find_k_distant_indices(nums, key, k):
    keys = list()
    for i in range(len(nums)):
        if nums[i] == key:
            keys.append(i)
    out = list()
    for i in range(len(nums)):
        for key in keys:
            if abs(i-key) <= k:
                out.append(i)
                break
    return out


print(find_k_distant_indices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1))
