def minimum_abs_difference(arr):
    arr.sort()
    m = float('inf')
    for i in range(len(arr) - 1):
        m = min(m, abs(arr[i] - arr[i + 1]))

    out = list()
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i+1]) == m:
            out.append((arr[i], arr[i+1]))
    return out


print(minimum_abs_difference([4, 2, 1, 3]))
