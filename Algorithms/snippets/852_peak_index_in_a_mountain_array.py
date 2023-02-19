def peak_index_in_mountain_array(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) / 2
        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return l


print(peak_index_in_mountain_array([0, 10, 5, 2]))
