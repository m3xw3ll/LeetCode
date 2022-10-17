def count_distinct_integers(nums):
    nums = set(nums)
    out = list()
    for i in nums:
        out.append(int(str(i)[::-1]))
    out += list(nums)
    return len(set(out))


print(count_distinct_integers([1, 13, 10, 12, 31]))
