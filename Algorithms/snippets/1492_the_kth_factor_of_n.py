def kth_factor(n, k):
    for i in range(1, n+1):
        if n % i == 0:
            k -= 1
        if k == 0:
            return i
    return -1


print(kth_factor(7, 2))