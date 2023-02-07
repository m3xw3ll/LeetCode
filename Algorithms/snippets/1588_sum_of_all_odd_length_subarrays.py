def sum_odd_length_subarrays(arr):
    s = 0
    n = len(arr)

    for i in range(1, n + 1, 2):
        for j in range(n - i + 1):
            s += sum(arr[j:j+i])
    return s


print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))
