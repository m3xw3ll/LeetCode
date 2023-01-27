def contains_pattern(arr, m, k):
    cnt = 0
    for i in range(len(arr) - m):

        if arr[i] == arr[i+m]:
            cnt += 1
        else:
            cnt = 0

        if cnt == (k - 1) * m:
            return True
    return False


print(contains_pattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
