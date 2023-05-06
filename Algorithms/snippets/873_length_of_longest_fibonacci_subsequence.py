def longest_fib_subseq(arr):
    s = set(arr)
    res = 2
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a, b, l = arr[i], arr[j], 2
            while a + b in s:
                a, b, l = b, a + b, l + 1
            res = max(res, l)
    return res if res > 2 else 0


print(longest_fib_subseq([1, 2, 3, 4, 5, 6, 7, 8]))
