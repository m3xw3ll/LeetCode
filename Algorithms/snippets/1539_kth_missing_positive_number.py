def find_kth_positive(arr, k):
    arr = set(arr)
    for i in range(1, 10000):
        if i not in arr:
            if k == 1:
                return i - 1
            k -= 1



print(find_kth_positive(arr = [1,2,3,4], k = 2))
