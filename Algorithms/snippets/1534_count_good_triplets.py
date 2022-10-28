def count_good_triplets(arr, a, b, c):
    cnt = 0
    l = len(arr)

    for i in range(l):
        for j in range(i+1, l):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, l):
                    if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                        cnt += 1
    return cnt


print(count_good_triplets([7,3,7,3,12,1,12,2,3], 5, 8, 1))
