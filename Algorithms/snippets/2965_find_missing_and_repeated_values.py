def find_missing_and_repeated_values(grid):
    flat = [j for sub in grid for j in sub]
    flatset = set()

    for n in flat:
        if n in flatset:
            dup = n
        else:
            flatset.add(n)

    miss = [ele for ele in range(1, len(grid)**2 + 1) if ele not in flat]
    return [dup, miss[0]]


print(find_missing_and_repeated_values([[1, 3], [2, 2]]))
