def sum_of_unique(nums):
    unique = set(nums)
    not_unique = set()

    for n in nums:
        if n in not_unique and n in unique:
            unique.remove(n)
        not_unique.add(n)

    return sum(list(unique))


print(sum_of_unique([1, 2, 3, 4, 5]))
