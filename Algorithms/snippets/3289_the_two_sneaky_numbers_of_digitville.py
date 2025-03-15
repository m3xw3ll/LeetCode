def get_sneaky_numbers(nums):
    seen = set()
    dups = set()
    for i in nums:
        if i in seen:
            dups.add(i)
        else:
            seen.add(i)
    return list(dups)


print(get_sneaky_numbers([0, 1, 1, 0]))