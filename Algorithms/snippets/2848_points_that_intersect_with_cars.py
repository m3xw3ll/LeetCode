def number_of_points(nums):
    out = set()
    for pair in nums:
        for i in range(pair[0], pair[1] + 1):
            out.add(i)
    return len(out)


print(number_of_points(nums=[[1, 3], [5, 8]]))
