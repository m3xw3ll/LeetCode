def can_make_arithmetic_progression(arr):
    arr = sorted(arr)
    diff = [arr[n] - arr[n - 1] for n in range(1, len(arr))]
    return all([diff[0] == diff[n] for n in range(1, len(diff))])


print(can_make_arithmetic_progression([3, 5, 1]))
