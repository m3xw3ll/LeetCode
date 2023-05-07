def majority_element(nums):
    m = len(nums) / 3
    out = []
    for n in set(nums):
        if nums.count(n) > m:
            out.append(n)
    return list(set(out))


print(majority_element([1, 2]))
