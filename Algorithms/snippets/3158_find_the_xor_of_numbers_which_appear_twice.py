def duplicate_numbers_xor(nums):
    seen = set()
    dups = set()
    out = 0
    for n in nums:
        if n in seen:
            dups.add(n)
        else:
            seen.add(n)

    for i in dups:
        out ^= i
    return out


print(duplicate_numbers_xor(nums=[1, 2, 2, 1]))