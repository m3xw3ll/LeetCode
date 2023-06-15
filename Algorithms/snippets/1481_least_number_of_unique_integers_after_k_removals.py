from collections import Counter


def find_least_num_of_unique_ints(arr, k):
    c = Counter(arr)
    cnt = Counter(c.values())
    rem = len(c)
    for i in sorted(cnt):
        if k >= i * cnt[i]:
            k -= i * cnt[i]
            rem -= cnt.pop(i)
        else:
            return rem - k // i
    return rem


print(find_least_num_of_unique_ints(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
